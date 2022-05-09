// //alert("TESST")
// function getCookie(name) {
//   let cookieValue = null;
//   if (document.cookie && document.cookie !== '') {
//       const cookies = document.cookie.split(';');
//       for (let i = 0; i < cookies.length; i++) {
//           const cookie = cookies[i].trim();

//           if (cookie.substring(0, name.length + 1) === (name + '=')) {
//               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//               break;
//           }
//       }
//   }
//   return cookieValue;
// }
// const csrftoken = getCookie('csrftoken');



// doc_add.onsubmit = async (e) => {
//     e.preventDefault();

//     let response = await fetch('/example', {
//       method: 'POST',
//       body: new FormData(doc_add),
//       headers: { "X-CSRFToken": csrftoken }
//     });
//     document.getElementById("formElem").reset()
    
//     let result = await response.json();

//     alert(result.message);
//   };

function change_save(){
  alert("Heelolol")
}







































// const p = document.getElementById("try").innerHTML
// let btn = document.getElementById("btn");
// btn.addEventListener('click', event => {
//     alert("WORKS")
    
      
// });


// $.ajax({

//     type : 'POST',
  
//     url:'http://localhost:8000/example',
  
//     data:{
//      username: 'UGHHHHHH',
//      csrfmiddlewaretoken: csrftoken
//     },
  
//    success:function(data){
       
//    }
//   });