import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    const path = process.argv[2];
    readDatabase(path)
      .then((fields) => {
        let output = 'This is the list of our students\n';
        const sortedFields = Object.keys(fields).sort(
          (a, b) => a.toLowerCase().localeCompare(b.toLowerCase()),
        );
        for (const field of sortedFields) {
          const count = fields[field].length;
          const list = fields[field].join(', ');
          output += `Number of students in ${field}: ${count}. List: ${list}\n`;
        }
        response.status(200).send(output.trim());
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    const path = process.argv[2];
    readDatabase(path)
      .then((fields) => {
        const names = fields[major] || [];
        response.status(200).send(`List: ${names.join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
