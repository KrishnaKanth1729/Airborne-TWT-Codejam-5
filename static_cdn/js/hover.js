var lolo = [...document.querySelectorAll(".loc-button")]

lolo.forEach(lol => {
    lol.addEventListener("click", () => {
    event.preventDefault()
    window.scrollTo(0, window.scrollY + document.querySelector('#scroll-bar').getBoundingClientRect().top)
})
})

