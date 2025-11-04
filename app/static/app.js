
const a=document.getElementById("a"),b=document.getElementById("b"),op=document.getElementById("op"),
btn=document.getElementById("btn"),result=document.getElementById("result");
btn.addEventListener("click",async()=>{result.textContent="…";try{const resp=await fetch("/api/calc",{method:"POST",
  headers:{"Content-Type":"application/json"},body:JSON.stringify({a:Number(a.value),b:Number(b.value),op:op.value})});
  if(!resp.ok){const err=await resp.json();result.textContent=`Error: ${err.detail||resp.statusText}`;return}
  const data=await resp.json();result.textContent=data.result}catch(e){result.textContent=`Error: ${e.message}`}});
