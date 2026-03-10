const fileInput = document.getElementById('file');
const fileNameSpan = document.getElementById('file-name');
fileInput.addEventListener('change', function() {
    if (this.files && this.files.length > 0) {
        let name = this.files[0].name;
        if(name.length > 25) {
            name = name.substring(0, 22) + "...";
        }
        fileNameSpan.textContent = name;
        fileNameSpan.style.color = "#333"; 
        // 
        } else {
            fileNameSpan.textContent = "No file chosen.";
            fileNameSpan.style.color = "#777";
        }
    });