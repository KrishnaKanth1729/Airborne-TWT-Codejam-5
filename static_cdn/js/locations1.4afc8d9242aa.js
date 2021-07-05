let visitedButton = [...document.querySelectorAll('.visit')]
let favouriteButtons = [...document.querySelectorAll('.fav')]
let cards = [...document.querySelectorAll('.box')]
let search = document.querySelector("#search")
let btn = document.querySelector("#formButton")
let reviewButtons = [...document.querySelectorAll('.delete-review')]
let reviews = [...document.querySelectorAll('.user-review')]
console.log(reviews)
 console.log(favouriteButtons)
let favboxes = [...document.querySelectorAll('.favbox')]
favouriteButtons.forEach(button => {
    button.addEventListener("click", () => {
        $.ajax({
        url: 'https://holidayplanner.kk1729.repl.co/favourite/' + button.id.toString().split('-')[0],
        dataType: 'json',
        success: function (data) {
          if (data.type === 1){
              alert(1)
              button.classList.remove('fas')
              button.classList.add("far")
              console.log(button.id)
              document.getElementById(button.id.toString().split('-')[0] + '-favbox').style.display = 'none'
              favboxes.splice(favboxes.indexOf(document.getElementById(button.id.toString().split('-')[0] + '-favbox')))
              if (favboxes.length === 0){
                  console.log("finished")
              }
          }
        }  
    });
    })
})

reviewButtons.forEach(button => {
    button.addEventListener("mouseover", () => {
        button.style.color = 'red'
    })

    button.addEventListener("mouseout", () => {
        button.style.color = 'initial'
    })
    button.addEventListener("click", () => {
         $.ajax({
        url: 'https://holidayplanner.kk1729.repl.co/delete_review/' + button.id,
        dataType: 'json',
        success: function (data) {
          if (data) {
              if (document.getElementById(button.id + 'review').classList.contains('far')){
            document.getElementById(button.id + 'review').style.display = 'none';
            reviews.splice(reviews.indexOf(document.getElementById(button.id + 'review')), 1)
            }
            
            if (reviews.length === 0){
                document.getElementById("no-review-text").innerText = 'No reviews yet'
            }
        }
        }
    });
    });
});

visitedButton.forEach(button => {
    button.addEventListener("click", () => {
        event.preventDefault()
      $.ajax({
        url: 'https://holidayplanner.kk1729.repl.co/visit/' + button.id,
        dataType: 'json',
        success: function (data) {
          if (data.type === '2') {
              alert("Added to visited List. Check your profile for more. https://holidayplanner.kk1729.repl.co/user/profile")
            button.classList.remove("fa-times-circle")
          button.classList.add('fa-check-circle')
          button.style.fontsize = '5rem'
          button.style.color = 'green'
          } else if(data.type === '1'){
              alert("asda")
            button.classList.remove("fa-check-circle")
          button.classList.add('fa-times-circle')
          button.style.fontsize = '5rem'
          button.style.color = 'red'
          }
          
    //do what you need here
    setTimeout(function(){
        document.getElementById(button.id + '-box').style.display = 'none'
      }, 300);
    
           
console.log(cards)
cards.splice(cards.indexOf(document.getElementById(button.id+'-card')), 1)
if (cards.length === 0){
    document.getElementById("no-card-heading").style.display  = ''
}          
        }
      });

    })
})
function redirect(query){
    search.value = query
    btn.click()
}
