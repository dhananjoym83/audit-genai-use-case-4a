import streamlit as st
import process as pr
from process import *

def main():
    st.title("File Uploader")

    # Create three file upload boxes
    call_transcript = st.file_uploader("Upload Call Transcript", type=["txt", "pdf"])
    # peer1_fs = st.file_uploader("Upload Peer 1 FS", type=["txt", "pdf"])
    # peer2_fs = st.file_uploader("Upload Peer 2 FS", type=["txt", "pdf"])

    # Create a text box to display process status
    status_text = st.empty()

    # Create a button to start processing
    if st.button("Process File"):
        # Check if all files are uploaded
        if call_transcript is not None:
            # Update status text
            status_text.text("Processing file...")

            # Perform processing here
            # ...

            # Update status text
            status_text.text("File processed successfully.")

            # Create a download button
            st.download_button("Download Processed File", data=processed_file, file_name="processed_file.zip", mime="application/zip")
        else:
            # Update status text
            status_text.text("Please upload all files.")

if __name__ == "__main__":
    main()
