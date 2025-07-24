const newman = require('newman');
const path = require('path');

newman.run({
  collection: path.join(__dirname, 'jsonplaceholder.postman_collection.json'),
  reporters: ['htmlextra', 'junitfull'],
  reporter: {
    htmlextra: { export: './report.html' },
    junitfull: { export: './report.xml' }
  }
}, (err) => {
  if (err) { throw err; }
  console.log('Test run completed!');
});