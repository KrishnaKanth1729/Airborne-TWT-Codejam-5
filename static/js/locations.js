let visitedButton = [...document.querySelectorAll('.visit')]
let searches = [...document.querySelectorAll('.search-history')]

searches.forEach(search => {
    search.addEventListener("click", () => {
        event.preventDefault()
        $.ajax({
        url: 'https://airborne.kk1729.repl.co/visit/' + button.id,
        dataType: 'json',
        success: function (data) {
          if (data) {
              
          } 
          
          
        }
      });
    })
})

visitedButton.forEach(button => {
    button.addEventListener("click", () => {
        event.preventDefault()
      $.ajax({
        url: 'https://airborne.kk1729.repl.co/visit/' + button.id,
        dataType: 'json',
        success: function (data) {
          if (data.type === '2') {

            button.classList.remove("fa-times-circle")
          button.classList.add('fa-check-circle')
          button.style.fontsize = '5rem'
          button.style.color = 'green'
          } else if(data.type === '1'){
            button.classList.remove("fa-check-circle")
          button.classList.add('fa-times-circle')
          button.style.fontsize = '5rem'
          button.style.color = 'red'
          }
          
          
        }
      });

    })
})

