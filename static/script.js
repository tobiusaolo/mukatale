const cname =document.getElementById('c_name');
const cemail = document.getElementById('c_email');
const fm =document.getElementById('formValidate0');
const erroElement =document.getElementById('error');

fm.addEventListener('submit' ,(e) =>{
    let message = []
    if(cname.value ==='' || cname.vlaue == null){
        message.push("company name is required")
    }

    if(message.length>0){
        e.preventDefault()
        erroElement.innerText = message.join(',')
    }
});