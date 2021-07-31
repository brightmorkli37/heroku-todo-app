// alert("hello world!")

const button = document.querySelector('button')

button.onmouseover = () => {
    button.style.backgroundColor = 'cyan';
    setTimeout(() => button.style.backgroundColor = 'black', 2000)
}
