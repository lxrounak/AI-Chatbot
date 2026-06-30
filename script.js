async function send(){
let m=document.getElementById("msg").value;
let c=document.getElementById("chat");
c.innerHTML+=`<p><b>You:</b> ${m}</p>`;
let r=await fetch("/chat",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({message:m})});
let d=await r.json();
c.innerHTML+=`<p><b>AI:</b> ${d.reply}</p>`;
document.getElementById("msg").value="";
}
