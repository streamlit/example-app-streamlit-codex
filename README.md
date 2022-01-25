
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/streamlit/example-app-streamlit-codex/main)

<img src="https://user-images.githubusercontent.com/27242399/150765835-8694a961-161e-4f97-bb29-cbc1fce426cb.png" width="500"/>

A Streamlit app that builds Streamlit apps!


### How to use our Codex app

Here are a few sample apps to get you started:

![image](https://user-images.githubusercontent.com/27242399/150765383-817c9cfb-9d00-497d-9aee-a35f39f255fa.png)


The text prompt is where the magic starts.

First, explain to Codex what app you’d like to create. For example, create a web app that shows Google stocks in a particular date range. When done, generate the code by clicking on the Execute button:

![image](https://user-images.githubusercontent.com/27242399/150765453-de38e26d-509c-497b-80db-422eb539dd4e.png)

Next, tweak the settings and edit the Codex output. Once Codex generates the code, you’ll see a second prompt. Review the code and edit it if you spot any issues:

![image](https://user-images.githubusercontent.com/27242399/150765487-395131fd-fa1c-4dfe-9b4f-0398a53870cd.png)

Happy with your prompt? It’s time to generate the code to launch your Streamlit app! I’ve used the Python exec function and this code snippet:


```
button3 = st.button("🎈 Execute Code")
    if button3:
        exec(output_code)Le
```

That’s it. Sit back, relax, and watch your app launch!

![image](https://user-images.githubusercontent.com/27242399/150766907-96aaa811-2551-459e-bf5d-5786f3e132e0.png)

<img src="![image](https://user-images.githubusercontent.com/27242399/150765541-817e5f21-ab5b-498c-a992-6c9338eb825d.png)" width="500"/>


