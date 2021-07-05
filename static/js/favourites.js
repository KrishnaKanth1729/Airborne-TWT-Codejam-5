let favButtons = [...document.querySelectorAll('.fav')]
favButtons.forEach(button => {
    button.addEventListener("click", () => {
        var pk = button.id.toString().split('-')[0]
    $.ajax({
        url: 'https://airborne.kk1729.repl.co/favourite/' + pk,
        dataType: 'json',
        success: function (data) {
          if (data.type === 1) {
            button.classList.remove('fas')
          button.classList.add('far')
          } else if (data.type === 2){
          button.classList.remove('far')
          button.classList.add('fas')
        }
          
        } 
      });

    });
    })
    
