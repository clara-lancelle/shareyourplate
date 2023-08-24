console.log(document.querySelector('input-image'))
let input_image = document.querySelector('.input-image')

if (input_image.value) {
    document.querySelector('#input-image-value').innerHTML = `Image uploadée : ${input_image.value}`
}

input_image.addEventListener('change', ()=> {
    let val = document.querySelector('.input-image').value
    document.querySelector('#input-image-value').innerHTML = `Image uploadée : ${val}`
})   