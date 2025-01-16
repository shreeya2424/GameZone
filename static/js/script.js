document.addEventListener("DOMContentLoaded", () => {
    // const array = ['hat', 'house', 'rat', 'cat', 'leaf', 'clock', 'dog'];
    // const word = array[Math.floor(Math.random() * array.length)];
    // console.log(word)

    console.log("hello bhai")
    const button = document.getElementById("bc")
    console.log(button) //undefined bolra bc

    if (!button) {
        console.error("Element(s) not found. Check your HTML for correct IDs.");
        return;
    }
    const wordtoguess = document.getElementById['wordtoguess']
    console.log(wordtoguess.innerText)
    button.addEventListener('click', () => {
        if (wordtoguess.style.display === 'none') {
            // wordtoguess.innerText = word;
            // wordtoguess.style.display = 'inline';
            // btn.textContent = 'Hide Word';
            console.log('entered if')
        } else {
            // wordtoguess.style.display = 'none';
            // btn.textContent = 'Show Word'
            console.log('entersed else')
        }
    });
});
