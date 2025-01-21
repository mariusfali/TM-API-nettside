// fetch('databasetest.txt')
//     .then(response => response.text())
//     .then(text => console.log(text))

function getSampleText(){
    console.log(fetch("databasetest.txt", Headers).text())
}

getSampleText()