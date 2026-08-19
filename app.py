import streamlit as st
from PIL import Image
from io import BytesIO

from prompts import get_characters, get_scenes, build_prompt
from cropper import crop_character

st.set_page_config(page_title="KOCI AI Studio", layout="wide")

st.title("🐱 KOCI AI STUDIO")
st.caption("Streamlit UI untuk menyiapkan karakter + prompt sebelum generate video di backend Colab.")

with st.sidebar:
    st.header("Backend Colab")
    backend_url = st.text_input(
        "Tempel URL backend Colab / Gradio di sini",
        placeholder="https://xxxx.gradio.live"
    )
    if backend_url:
        st.success("Backend URL tersimpan.")
        st.link_button("🔗 Open Backend", backend_url)

st.subheader("1) Upload Master Character Sheet")
uploaded = st.file_uploader(
    "Upload gambar master sheet keluarga kucing",
    type=["png", "jpg", "jpeg"]
)

if uploaded:
    master_image = Image.open(uploaded).convert("RGB")

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.image(master_image, caption="Master Sheet", use_container_width=True)

    with col2:
        st.subheader("2) Pilih Karakter & Scene")

        character = st.selectbox("Character", get_characters())
        scene_options = get_scenes(character)
        scene_name = st.selectbox("Scene", scene_options)

        prompt = build_prompt(character, scene_name)
        prompt = st.text_area("Prompt", value=prompt, height=220)

        duration = st.radio("Durasi", ["2 sec", "3 sec", "5 sec"], horizontal=True)

        if st.button("✅ Prepare Scene", use_container_width=True):
            cropped = crop_character(master_image, character)

            st.session_state["cropped"] = cropped
            st.session_state["prompt"] = prompt
            st.session_state["character"] = character
            st.session_state["scene_name"] = scene_name
            st.session_state["duration"] = duration

if "cropped" in st.session_state:
    st.divider()
    st.subheader("3) Hasil Prepare")

    col3, col4 = st.columns([1, 1])

    with col3:
        st.image(
            st.session_state["cropped"],
            caption=f"Preview Crop — {st.session_state['character']}",
            use_container_width=True
        )

    with col4:
        st.markdown(f"**Character:** {st.session_state['character']}")
        st.markdown(f"**Scene:** {st.session_state['scene_name']}")
        st.markdown(f"**Durasi:** {st.session_state['duration']}")
        st.text_area(
            "Prompt Final",
            st.session_state["prompt"],
            height=220,
            key="prompt_final_readonly"
        )

        # download image
        img_buffer = BytesIO()
        st.session_state["cropped"].save(img_buffer, format="PNG")
        img_buffer.seek(0)

        st.download_button(
            label="⬇ Download Cropped Image",
            data=img_buffer,
            file_name=f"{st.session_state['character'].lower()}_input.png",
            mime="image/png",
            use_container_width=True
        )

        # download prompt
        st.download_button(
            label="⬇ Download Prompt TXT",
            data=st.session_state["prompt"],
            file_name=f"{st.session_state['character'].lower()}_prompt.txt",
            mime="text/plain",
            use_container_width=True
        )

    st.info(
        "Langkah berikutnya: buka backend Colab, upload cropped image ini, "
        "paste prompt final, lalu generate video."
    )
else:
    st.warning("Upload master sheet dulu, lalu pilih karakter dan scene.")
