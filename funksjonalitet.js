fetch('./temp_database.txt')
    .then(response => response.text())
    .then(text => console.log(text))

