import streamlit as st
from streamlit_ace import st_ace
import toml
import openai


@st.experimental_memo(suppress_st_warning=True)  # type: ignore
def complete_code(input_code: str, codex_args: dict) -> str:
    """Call OpenAI Codex to convert input code into output code."""
    # Load your API key from an environment variable or secret management service
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    # Display a funny mouse moving animation.
    mouse_gif = st.columns(3)[1].image("mouse.gif")

    # Complete the code
    try:
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=input_code,
            echo=True,
            **codex_args,
        )
        return response["choices"][0]["text"]
    finally:
        mouse_gif.empty()


def rows_of_three(width_ratio=7):
    """A generator of containers aranged in rows of three."""
    while True:
        for col in st.columns([width_ratio, 1, width_ratio, 1, width_ratio])[::2]:
            yield col


def main():
    """Execution starts here."""
    # Header
    title = "Streamlit App Builder"
    st.set_page_config(page_title=title, page_icon="✨")  # type: ignore
    # st.image("logoNew.png")
    st.image("logo.png")

    # These two TOML files describe possible modes and codex parameters, respectively.
    codex_params = toml.load("codex_params.toml")["codex_params"]
    modes = list(toml.load("modes.toml")["modes"].values())

    def reset_state():
        """Reset the state to mode defaults."""
        defaults = {key: input["default_value"] for key, input in codex_params.items()}
        st.session_state.update(defaults)
        st.session_state.update(st.session_state.mode["codex_args"])
        st.session_state.execute_code = False
        st.session_state.output_code = ""
        st.session_state.state_initialized = True

    # Let the user select an input mode
    get_title = lambda mode: mode["title"]
    mode = st.selectbox(
        "Code sample", modes, format_func=get_title, on_change=reset_state, key="mode"
    )
    if not st.session_state.get("state_initialized"):
        reset_state()

    # Let the user set the input code.
    input_code = st_ace(value=mode["input_code"], language="python", auto_update=True)

    # Draw a grid of inputs.
    codex_args = {}
    with st.form("Codex settings"):
        st.caption("Codex settings")
        for (key, input), container in zip(codex_params.items(), rows_of_three()):
            widget_func = getattr(container, input["input_type"])
            codex_args[key] = widget_func(label=key, key=key, **input["input_params"])

        # Empty lists cannot be passed in as codex_args. This only applies to "stop".
        if len(codex_args["stop"]) == 0:
            del codex_args["stop"]

        # Clicking the button Unchecks the "execute_code" checkbox.
        def uncheck_execute_code():
            st.session_state.execute_code = False

        if st.form_submit_button("Generate Code", on_click=uncheck_execute_code):
            st.session_state.output_code = complete_code(input_code, codex_args)

    output_code = st.session_state.get("output_code", "")
    output_code = st_ace(value=output_code, language="python", auto_update=True)

    # The "output_controls" dict defines any final output controls.
    output_controls = mode.get("output_controls", {})

    # If "execute_button" is defined, then display it.
    if "execute_button" in output_controls:
        if st.checkbox(output_controls["execute_button"], key="execute_code"):
            exec(output_code, globals())

    # If "download_button" is defined, then display it.
    if "download_button" in output_controls:
        st.download_button(output_controls["download_button"], output_code)

    st.caption(
        "Created with [Streamlit](https://streamlit.io/) and "
        "[OpenAI Codex](https://openai.com/blog/openai-codex/). "
        "Get your own [Codex API key](https://openai.com/blog/api-no-waitlist/)!"
    )


if __name__ == "__main__":
    main()
