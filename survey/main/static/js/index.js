//0-1. 전역 변수
var date = new Date();
year = date.getFullYear();
month = date.getMonth();
day = date.getDate();
jQuery(function($){
    //0. 기본 변수
    var $win = $(window);
    var $doc = $(document);
    
    //2-1. gamebtn/lnbbtn 변수
	var	$gamebtn = $(".gamebtn");
	var	$gamelist = $(".gamelist");
	var	$gamebtnToggle = $(".gamebtnToggle");
	var	$main = $("#main");
	var	$lnbbtn = $(".lnbbtn");
	var	$lnbMenu = $(".lnbMenu");
	var	$footer = $("footer");
    var toggleOn = false;
    var $header_single = $('.header_single');
    //2-2. gamebtn 토글 버튼	
	$gamebtn.on('click',function(){
        if($main.is(':animated') || $lnbbtn.is(':animated') || $lnbbtn.is(':animated') || $lnbMenu.is(':animated')  || $footer.is(':animated') ){
           return;
        }
        var mainPosition = $header_single.offset().left;
        $gamelist.toggle("slide");
        if($gamebtnToggle.text() == '추천메뉴 열기'){
            $gamebtnToggle.text('추천메뉴 닫기');
            $main.animate({left: '118px'});
            var target = 0;
                if(toggleOn === false){
                    target = mainPosition+118;
                }else{
                    target = mainPosition+268;   
                    $lnbMenu.animate({left: target-150});
                }
                $lnbbtn.animate({left: target});
                $footer.animate({left: '118px'});
                
        }else{
            $gamebtnToggle.text('추천메뉴 열기');
            $main.animate({left: '0'});
            var target2 = 0;
                if(toggleOn === false){
                    target2 = mainPosition+0;
                }else{
                    target2 = mainPosition+150;   
                    $lnbMenu.animate({left: target2-150});
                }
                $lnbbtn.animate({left:target2});
                $footer.animate({left: '0px'});         
        }
    });	

    
    //2-3. lnbbtn 토글 버튼
    var $lnbbtnToggle = $('.lnbbtnToggle');
    $('.lnbbtn').on('click',function(event){
        var $this = $(this);
        var mainPosition = $header_single.offset().left;
        if($this.is(':animated') || $lnbMenu.is(':animated')){
           return;
        }
        if(toggleOn === false){
            $win.on("mousewheel.disableScroll DOMMouseScroll.disableScroll touchmove.disableScroll", function(e) {
                e.preventDefault();
                return;
            });//스크롤 막기
            
            $lnbbtnToggle.text('메뉴 닫기');
            if($gamebtnToggle.text() === '추천메뉴 열기'){
                $this.animate({left: mainPosition+150},300);
//                $this.find('img').rotate({angle:180});
                $lnbMenu.css({display: 'block'});
                $lnbMenu.animate({left: mainPosition+0},300);
            }else{
                $this.animate({left: mainPosition+268},300);
                $lnbMenu.css({display: 'block'});
                $lnbMenu.animate({left: mainPosition+118},300);
            }
            toggleOn = true;
        }else{
            
            $lnbbtnToggle.text('메뉴 열기');
            if($gamebtnToggle.text() === '추천메뉴 열기'){
                $this.animate({left: mainPosition},300);
                $lnbMenu.animate({left: -1000},300);
            }else{
                $this.animate({left: mainPosition+118},300);
                $lnbMenu.animate({left: -1000},300);
            }
            $win.off(".disableScroll");//스크롤 막기
            toggleOn =false;
        }
    });
    
    
    
    //4-1. lnbMenu ul>li>a 색상 넣기
    $('.lnbMenu > ul >li :even').css({background:'#fff'});
    $('.lnbMenu > ul >li :odd').css({background:'#fff'});

    //5-1. mainLiRemovest 변수
    var $mainLiRemovest = $('#main> ul >li');
    var $writeUserInfor = $('.writeUserInfor');
    var $userPic = $('.userPic');
    var $emptyPic = $('.emptyPic');
    var $connectUser = $('.connectUser');
    var $countView = $('.countView');
    
    //5-2. mainLiRemovest height 가변 값 만들기
    function mainLiRemovestHeight(x,y){
        $mainLiRemovest.css({height:x+y+10});
        $writeUserInfor.css({height: x-8});
        $userPic.css({height:x-12}).css({width:x-12});
        $emptyPic.css({height:x-12}).css({width:x-12});
        $connectUser.css({height: x});
        $countView.css({top:x+y});        
    }
    mainLiRemovestHeight(60,30);

    //6-1. scroll조작 시 head_single, bottommenu 보이고,사라지고...
    var prevScrollTop = 0;
    var $bottommenu = $('.bottommenu');
    $header_single.css({visibility:'visible'});
    $bottommenu.css({visibility:'visible'});
    $win.on('scroll', function(event){
        var $this = $(this);
        var scrollTop = $this.scrollTop();
        //6-2. 변수: scroll의 이전위치, 현재위치 체크
        //(6-2)의 class 추가/삭제를 이용해 .is() 체크
        if(scrollTop == prevScrollTop){
            $header_single.css({visibility: 'visible'}); 
            $bottommenu.css({visibility: 'visible'}); 
        }
        else if(scrollTop >= prevScrollTop){ //스크롤을 내릴 때 & 내리고 멈춘 상태
            if($gamelist.css("display") == 'block'){
                $header_single.css({visibility: 'visible'}); 
                $lnbbtn.css({visibility: 'visible'});                 
            }else{
                $header_single.css({visibility: 'hidden'}); 
                $bottommenu.css({visibility: 'visible'}); 
                $lnbbtn.css({visibility: 'visible'}); 
            }
        }else{ //스크롤을 올릴 때 & 올리고 멈춘 상태
            $header_single.css({visibility: 'visible'}); 
            $bottommenu.css({visibility: 'hidden'}); 
        }
        prevScrollTop = scrollTop;
    });
    $win.trigger('scroll');
    
    
    //2-5. lnbMenu 높이와 너비 맞추기
    $lnbbtn.on('click',function(event){
        //2-4.lnblist moving
        var head_singleHeight = $('.header_single').height();
        var bottommenuHeight = $('.bottommenu').height();
        var lnbHeight = $win.height()-head_singleHeight;
        var $lnbLi = $('.lnbMenu li');
        var $lnbLiA = $('.lnbMenu li >a');
        if($header_single.is('.v')){
            //위아래 다 보일 때
            if($bottommenu.is('.v')){
                $lnbMenu.css({top: head_singleHeight});
                $lnbMenu.css('height', lnbHeight-bottommenuHeight+'px');
            }
            //위만 보일 때
            else if($bottommenu.is('.h')){
                $lnbMenu.css({top: head_singleHeight});
                $lnbMenu.css('height',lnbHeight+'px');
            }
        }else if($header_single.is('.h')){
            $lnbMenu.css({visibility: 'visible'});
            //아래만 보일 때
            if($bottommenu.is('.v')){
                $lnbMenu.css({top: 0});
                $lnbMenu.css('height', lnbHeight+head_singleHeight-bottommenuHeight+'px');
            }
            //모두 안보일 때
            else if($bottommenu.is('.h')){
                $lnbMenu.css({top:0});
                $lnbMenu.css({height:lnbHeight+head_singleHeight});
            }
        }
    });
    //7-1. 색상 넣기
        
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
        $('.writeUserInfor').css({background:w});
        $('.header_single').css({background:x});
        $('.gamelist>li').css({background:x});
        $('#gamelistul li:nth-child(even)').css({background:x});
        $('#gamelistul li:nth-child(odd)').css({background:b});
        $('.search [type="search"]').css({background:x});
        $('.bottommenu').css({background:x});
        $('.header_body').css({background:y});
        $('#main>ul>li').css({background:z});
        $('.circle').css({background:z});
        $('.circle1').css({background:y});
        $('.scatchTape>div:nth-child(odd)').css('border-top','3.4px solid '+w);
        $('.scatchTape>div:nth-child(even)').css('border-bottom','3.4px solid '+w);

        $('.bottommenu > button').css({background:w});
        $('.overView >div').css({background:a});
        $('.write button').css({background:x});
        $('.write a').css({background:y});
    }
    mainColor(backColor[0],backColor[1],backColor[2],backColor[3], backColor[4], backColor[5]);
    
    //9-1. 리스트 선택 변수
    var $mainList = $('#main>ul>li');
    var preTop = 0;
    //9-2. 리스트 선택
    $mainList.on('click', function(event){
        var $this = $(this);
        var listHeight = $this.offset().top;
        var $mainListOther = $this.siblings();
        
        if($this.is(':animated')){
           return;
        }
        $this.css({background: backColor[1]})
            .find('.scatchTape>div:nth-child(odd)').css('border-top','3.4px solid '+backColor[5]).end()
            .find('.scatchTape>div:nth-child(even)').css('border-bottom','3.4px solid '+backColor[5]).end()
            .find('.writeUserInfor').css({background: backColor[5]}).end()
            .find('.circle').css({background: backColor[1]}).end()
            .siblings().css({background: backColor[3]})
                .find('.scatchTape>div:nth-child(odd)').css('border-top','3.4px solid '+backColor[0]).end()
                .find('.scatchTape>div:nth-child(even)').css('border-bottom','3.4px solid '+backColor[0]).end()
                .find('.writeUserInfor').css({background: backColor[0]}).end()
                .find('.circle').css({background: backColor[3]});
            
        if($this.is('.listOn')){//열려 있을 때
            $this.removeClass('listOn')
                .css({display:'block'})
                .find('.overView').slideUp(200);
            $mainListOther.toggle('slide')
                .css({display:'block'}).end();
            $this.css({height: 'auto'});
            $this.find('.clip').css({display:'block'});
            $('html,body').animate({'scrollTop':preTop},200);
        }else{//닫혀 있을 때
            preTop = $win.scrollTop();
            $header_single.css({visibility:'visible'});
            $this.addClass('listOn').css({display:'block'}).find('.overView').slideDown(200).end()
                .css({height : 'auto'},200);
            var articleHeight = parseInt($this.css('height').slice(0,-2));
            var image = parseInt($this.find('article').css('height').slice(0,-2));
            console.log(articleHeight);
            console.log(image);
            $this.css({height:articleHeight+image+80});
            //댓글이 달리면 이에 따라 80px값을 늘려주도록 넣어야 함
            $mainListOther.css({display:'block'}).toggle('slide');
            $('html,body').animate({'scrollTop':listHeight},200);
        }
    });
    var $refresh = $('.bottommenu img[src="./image/refresh.png"]');
    $refresh.on('click',function(event){
        $('html,body').animate({'scrollTop':0},0);
         
    });
});









