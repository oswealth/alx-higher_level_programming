#!/usr/bin/node

/* writes a string to a file.
    - the first argument is the file path.
    - the second argument is the string to write.
    - the content of the file is write in utf-8.
    - if an error occurred during the writing, prints the error object.
*/
const fs = require('fs');
const filename = process.argv[2];
const content = process.argv[3];

fs.writeFile(filename, content, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
