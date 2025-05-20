import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [skills, setSkills] = useState([]);

  const uploadResume = async () => {
    const formData = new FormData();
    formData.append('resume', file);

    const response = await axios.post('http://localhost:5000/upload', formData);
    setSkills(response.data.skills);
  };

  return (
    <div className="App">
      <h1>Resume Skill Extractor</h1>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={uploadResume}>Upload</button>
      <div>
        {skills.map((skill, i) => (
          <span key={i} style={{ border: "1px solid #ccc", padding: "5px", margin: "5px" }}>{skill}</span>
        ))}
      </div>
    </div>
  );
}

export default App;
