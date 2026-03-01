const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);
      let output = `Number of students: ${students.length}\n`;

      const fields = {};
      students.forEach((student) => {
        const studentData = student.split(',');
        const firstName = studentData[0];
        const field = studentData[3];
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstName);
      });

      for (const [field, names] of Object.entries(fields)) {
        output += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
      }
      
      output = output.trim();
      console.log(output);
      resolve(output);
    });
  });
}

module.exports = countStudents;
