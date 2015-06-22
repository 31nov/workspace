$(function($){
    //1-1. 색상 넣기
    var backColor = ['#f3bbcc','#6B78BF','#F6F1DB','#F294AD', '#3366cc', '#f2f2f2'];
//    var backColor = ['#f3bbcc','#233F61','#F6F1DB','#F294AD'];
//    var backColor = ['#F294AD','#F279A6','#C0D3C7','#7BA595'];
//    var backColor = ['#F2949C','#F2949C','#C0D3C7','#7BA595'];
//    var backColor = ['#DAD0D0','#233F61','#F6F1DB','#B57D9D'];
    
    function mainColor(w,x,y,z,a,b){
        //w: user 배경
        //x: 테두리
        //y: 배경
        //z: 리스트 배경
        $('.header_single').css({background:x});
        $('.header_body').css({background:y});
        $('.bottommenu').css({background:x});
    }
    mainColor(backColor[0],backColor[1],backColor[2],backColor[3], backColor[4], backColor[5]);
    
    //2-1. 로그인 폼 전달 전에 체크하기
    var $idInput = $('.idInput');
    var $pw = $('.pw');
    var $password = $('#createPassword');
    var $rePassword = $('#createRePassword');
    var $idText = $('.a p');
    var $passwordText = $('.b p');
    var $rePasswordText = $('.c p');
    var able1 = 0;
    var able2 = 0;
    
    function able(){
        console.log(able1+','+able2);
        if(able1==1 && able2 ==1){
            $('.createIn').removeAttr('disabled');   
        }else{
            $('.createIn').attr({disabled:'disabled'});   
        }
    }
    
    $idInput.on('keyup',function(){
        var str = $idInput.val();
        var exceptStr = str.match(/[^@.\+\-_\w ]+/g);
        if(exceptStr){
            $idText.text(exceptStr+'는 불가능합니다.').css({color:'#bf4040'});
            able1 = 0;
        }else{
            $idText.text('영문, 숫자, 특수문자( @ . + - _ )만 가능합니다.').css({color:'#000'});
            able1 = 1;
        }
        able();
    });
    $pw.on('keyup',function(){
        if($password.val().length >=4){
            $passwordText.text('비밀번호로 가능합니다.').css({color:'#5C9857'});
            if($password.val() === '' || $rePassword.val() === ''){
                $rePasswordText.text('비밀번호를 한번 더 써 주세요.').css({color:'#000'});
            }else if($password.val() == $rePassword.val()){
                $rePasswordText.text('비밀번호가 일치합니다.').css({color:'#5C9857'});
                able2= 1;
            }else{
                $rePasswordText.text('비밀번호가 일치하지 않습니다.').css({color:'#bf4040'});
                able2=0;
            }
        }else{
            $passwordText.text('비밀번호로 짧습니다.').css({color:'#bf4040'});
            able2=0;
        }
        able();
    });

});









