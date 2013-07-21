window.onload = function(){
  scrollTo(0,65535);
  var username = getCookie('username');
  if (username) document.post.name.value = username; 
}

function username(){
  var username = window.prompt("名前を入力しようか", document.post.name.value);
  if (username){
    document.post.name.value = username;
    setCookie('username', username, 30);
  }
}
