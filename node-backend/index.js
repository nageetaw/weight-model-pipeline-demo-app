// index.js
const express = require("express");
const axios = require("axios");
const app = express();
app.use(express.json());

const PY_API = process.env.PY_API || "http://localhost:8000"; // FastAPI base

app.post("/api/predict", async (req, res) => {
  try {
    const { height } = req.body;
    const r = await axios.post(`${PY_API}/predict`, { height });
    res.json(r.data); // {height, predicted_weight}
  } catch (err) {
    console.error(err.message);
    res.status(500).json({ error: "prediction failed" });
  }
});

const port = process.env.PORT || 3001;
app.listen(port, () => console.log(`Node backend listening on ${port}`));
