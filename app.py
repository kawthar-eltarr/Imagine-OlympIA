import streamlit as st
from stable import generate_image

def main():
    st.title("Imgine OlympIA : Stable Diffusion")

    prompt = st.text_input("Enter your prompt:")

    if st.button("Generate Image"):

        image = generate_image(prompt)

        st.image(image, caption="Generated Image", use_column_width=True, channels="RGB")

if __name__ == "__main__":
    main()
