window.onload = function(){
  scrollTo(0,65535);
  var username = getCookie('username');
  if (username) document.post.name.value = username; 
}

function change_name(){
  var username = window.prompt("名前を入力しようか", document.post.name.value);
  if (username){
    if (username.length > 15){
      window.alert('名前は15文字以内で( ´ー｀)');
      change_name();
    }
    else {
      document.post.name.value = username;
      setCookie('username', username, 30);
    }
  }
}
