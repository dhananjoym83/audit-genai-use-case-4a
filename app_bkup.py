import app_base as st

def main():
    st.title("File Uploader")

    # Create three file upload boxes
    client_fs = st.file_uploader("Upload Client FS", type=["txt", "pdf"])
    # peer1_fs = st.file_uploader("Upload Peer 1 FS", type=["txt", "pdf"])
    # peer2_fs = st.file_uploader("Upload Peer 2 FS", type=["txt", "pdf"])

    # Create a text box to display process status
    status_text = st.empty()

    # Create a button to start processing
    if st.button("Process Files"):
        # Check if all files are uploaded
        if client_fs is not None and peer1_fs is not None and peer2_fs is not None:
            # Update status text
            status_text.text("Processing files...")

            # Perform processing here
            # ...

            # Update status text
            status_text.text("Files processed successfully.")

            # Create a download button
            st.download_button("Download Processed Files", data=processed_files, file_name="processed_files.zip", mime="application/zip")
        else:
            # Update status text
            status_text.text("Please upload all files.")

if __name__ == "__main__":
    main()