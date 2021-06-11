function salir(){
    
(async() => {
    const{value: exit} = await Swal.fire({
         title: "¿Estas seguro de salir?",
         showClass: {
            popup: 'animate__animated animate__bounceIn'
          },
          hideClass: {
            popup: 'animate__animated animate__fadeOutUp'
          },
          
        icon: 'question',
        showCloseButton: true,

      
        inputValue:'exit',
        
       
    });
    if (exit){
        window.location.assign('/logout')
    }

})()
  
}

function eliminar(){
    
     Swal.fire({
        title: "¿Estas seguro de eliminar?",
        showConfirmButton: false,
              
         icon: 'error',

            
            
           
       
    
    })()
      
    }
    

    function inicio(){
    
        (async() => {
            const{value: inicio} = await Swal.fire({
                 title: "¿volver al inicio?",
                 showClass: {
                    popup: 'animate__animated animate__flipInY'
                  },
                  hideClass: {
                    popup: 'animate__animated animate__flipOutX'
                  },
                  
                icon: 'question',
                showCloseButton: true,
        
              
                inputValue:'inicio',
                
               
            });
            if (inicio){
                window.location.assign('/autenticacion')
            }
        
        })()
          
        }


        


 