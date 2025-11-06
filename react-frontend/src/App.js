import { useState } from "react";

export default function App() {
  const [height, setHeight] = useState("");
  const [weight, setWeight] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setWeight(null);
    try {
      const res = await fetch(`${process.env.REACT_APP_API_URL}/api/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ height: Number(height) }),
      });
      const data = await res.json();
      setWeight(data.predicted_weight);
    } catch (err) {
      alert("Request failed");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{ maxWidth: 480, margin: "40px auto", fontFamily: "sans-serif" }}
    >
      <h2>Height → Weight predictor (demo)</h2>
      <form onSubmit={handleSubmit}>
        <label>Height (cm):</label>
        <input
          value={height}
          onChange={(e) => setHeight(e.target.value)}
          type="number"
          required
        />
        <button disabled={loading} type="submit">
          {loading ? "Predicting..." : "Predict"}
        </button>
      </form>
      {weight !== null && (
        <p>
          Predicted weight: <strong>{weight.toFixed(2)} kg</strong>
        </p>
      )}
    </div>
  );
}
