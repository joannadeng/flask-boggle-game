let score = 0;
let secs = 60;
const words = new Set();

let timer = setInterval(tick,1000)
async function submitWord(evt) {
    evt.preventDefault();
    
   
    $(".msg").empty();
    let word = $('input').val();
    const res = await axios.get('/word',{params:{word:word}});
    console.log(res.data.result);
    // return res.data.result;
    
    if (res.data.result === "not-on-board" ) {
        $(".msg").text(`${word} is ${res.data.result}`)
      
    }else if(res.data.result === "not-word") {
        $(".msg").text(`${word} is ${res.data.result}`)
        
    }else if(words.has(word)){
        $(".msg").text(`${word} has been added`);

    }else{
        words.add(word);
        $(".msg").text(`${word} is added`)
        $("ul").append(`<li>${word}</li>`)
        score += word.length
        $(".score").text(`your current score is ${score}`)
        
    }
    $('input').val("");
    
}
$("form").on("click","button",submitWord)

async function tick(){
    secs -= 1;
    $(".secs").text(`Time Left: ${secs} seconds`);
    if(secs === 0){
        clearInterval(timer);
        $(".word").hide();
        $(".score").hide();
        $(".msg").text(`your final score is ${score}`)
        const resp = await axios.post('/gameOver',{score:score});
        console.log(resp);
    }
}


