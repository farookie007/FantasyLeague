var selectFields = document.querySelectorAll("#players input[type=checkbox");

selectFields.forEach((box) => {
    box.addEventListener("click", () => {
        console.log(box.parentElement.classList.toggle("selected"));
    })
})