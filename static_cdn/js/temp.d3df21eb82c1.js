let convertButtons = [...document.querySelectorAll('.convert')]
let temperatureText = [...document.querySelectorAll('.temp')]
let metrics = [...document.querySelectorAll('.metric')]
console.log(temperatureText)

console.log(convertButtons)

convertButtons.forEach(button => {
    button.addEventListener("click", () => {
        temperatureText.forEach(text => {
            var value = parseFloat(text.innerHTML)
            var length = value.toString().length
            console.log(value.toString().length)
            if (text.classList.contains('cel')){
                value = ((value * 9/5) + 32).toString();
                value = value.substring(0, length).toString()
                value = parseInt(value).toString()
                text.innerHTML = (parseInt(value).toFixed(0)).toString();  
                text.classList.remove('cel')
                text.classList.add('farenheit')
                metrics.forEach(metri => {
                    metri.innerHTML = '°F'
                })
            } else if (text.classList.contains('farenheit')){
                value = ((value - 32) * 5/9).toString();
                text.innerHTML = (parseInt(value).toFixed(1)).toString(); 
                text.classList.remove('farenheit')
                text.classList.add('cel')
                metrics.forEach(metri => {
                    metri.innerHTML = '°C'
                })
            }
        })
    })
})



