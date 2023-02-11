var body = {
    setColor:function(color){
        // document.querySelector('body').style.color = color;
        $('body').css('color',color);
    },
    setbackgroundcolor:function(color){
        // document.querySelector('body').style.backgroundColor = color;
        $('body').css('backgroundColor',color);
    }
}
var links = {
    setcolor:function(color){
    //     var alist = document.querySelectorAll('a');
    //     while(i<alist.length){
    //         alist[i].style.color=color;
    //         i++;
    //     }
    // }
    $('a').css('color',color);
    }
}
function day_night_handler(self){ 
    var target = document.querySelector('body');
    var i=0;
    if(self.value === 'night'){
        body.setbackgroundcolor('black');
        body.setColor('white');
        self.value = 'day';
        links.setcolor('powderblue');
    } else {
        body.setbackgroundcolor('white');
        body.setColor('black')
        self.value = 'night';
        i=0;
        links.setcolor('blue');
    }
}