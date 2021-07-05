var lolo = document.getElementsByClassName('loc-button')[0]


    lolo.addEventListener("click", () => {
    event.preventDefault()
    window.scrollTo(0, window.scrollY + document.querySelector('#scroll-bar').getBoundingClientRect().top)
})


