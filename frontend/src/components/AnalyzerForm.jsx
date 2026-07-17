import { useState } from "react";
import api from "../services/api";

function AnalyzerForm() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const analyzeComment = async () => {
    if (!text.trim()) {
      alert("Please enter a comment.");
      return;
    }

    try {
      const response = await api.post("/analyze", {
        text: text,
      });

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Failed to connect to backend.");
    }
  };

  return (
    <div>
      <h2>Analyze Comment</h2>

      <textarea
        rows="5"
        cols="70"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type a social media comment..."
      />

      <br />
      <br />

      <button onClick={analyzeComment}>
        Analyze
      </button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Result</h3>

          <p>
            <strong>Category:</strong> {result.category}
          </p>

          <p>
            <strong>Severity:</strong> {result.severity}
          </p>

          <p>
            <strong>Score:</strong> {result.score}
          </p>
        </div>
      )}
    </div>
  );
}

export default AnalyzerForm;