function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();

            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');
function add(){
    doc_add.onsubmit = async (e) => {
        e.preventDefault();
    
        let response = await fetch('/documents/add', {
          method: 'POST',
          body: new FormData(doc_add),
          headers: { "X-CSRFToken": csrftoken }
        });
        document.getElementById("doc_add").reset();
        window.location.href="/documents";
        
      };
}
function change_delete(){
      const str = location.href
        const replaced = str.replace(/\D/g, ''); 
        let rez = replaced.slice(4)
        console.log(rez);
        url = '/documents/' + rez + '/change';
      console.log("Im here");
      fetch(url, {
      method: 'DELETE',
      headers: { "X-CSRFToken": csrftoken }
    })
    window.location.href="/documents";
}
function change_save(){
     // Get Id from URL
     const str = location.href
     const replaced = str.replace(/\D/g, ''); 
     let rez = replaced.slice(4)
     console.log(rez);
  url = '/documents/' + rez + '/change';
   doc_change.onsubmit = async (e) => {
     e.preventDefault();
     let response = await fetch(url, {
       method: 'POST',
       body: new FormData(doc_change),
       headers: { "X-CSRFToken": csrftoken }
     });
     document.getElementById("doc_change").reset();
     
     // let result = await response.json();
 
     // alert(result.message);
   };
}
    
