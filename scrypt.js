 var submit = document.querySelector('.submit');
      var out = document.querySelector(".out");
      
      function aid(){
        var radios = document.getElementsByName('response');
        for(var i = 0; i < radios.length; i++){
          if(radios[i].checked){
            if(radios[i].value == "burn"){
              out.innerHTML = "okay now  you check if the area is safe.<br>\
                                okay now you put on gloves.<br>\
                                okay now you send frends to go get help.<br>\
                                okay now  you bandage the burn and wait for help to arrive.";
              break;
            }
            if(radios[i].value =="laceration"){
              out.innerHTML = "okay now you check if the area is safe.'<br>\
                              okay now you put on gloves.<br>\
                              okay now you send frends to go get help.<br>\
                              okay now you bandage the laceration and wait for help to arrive and do not\
                              use a turnekit unless absolutly nessecary."; 
              break;
            }
          }
        }
      }
      submit.addEventListener("click", aid);
