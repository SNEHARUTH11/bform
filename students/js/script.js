document.getElementById("uploadForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const fileInput = document.getElementById("file");
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("/students/upload/", {
        method: "POST",
        body: formData,
    });

    const message = document.getElementById("message");
    if (response.ok) {
        message.textContent = "File uploaded successfully!";
    } else {
        message.textContent = "Error uploading file.";
    }
});

document.getElementById("generateBForm").addEventListener("click", () => {
    window.location.href = "/students/generate-bform/";
});
