// index.js
const express = require("express");
const axios = require("axios");
const app = express();
app.use(express.json());

const cors = require("cors");
app.use(cors({ origin: "http://localhost:3000", methods: ["GET", "POST"] }));

const PY_API = process.env.PY_API;
// const PY_API = "http://127.0.0.1:8000";
if (!PY_API) console.warn("Warning: PY_API not set");

app.get("/", (req, res) =>
  res.json({ status: "Node App is working! Hurray :D" })
);

app.post("/api/predict", async (req, res) => {
  try {
    const { height } = req.body;
    console.log(PY_API);
    const r = await axios.post(`${PY_API}/api/predict`, { height });
    return res.json(r.data);
  } catch (e) {
    console.error("Prediction error:", e.message);
    return res.status(500).json({ error: "prediction failed" });
  }
});

const port = process.env.PORT || 3001;
app.listen(port, () => console.log(`Node-APE listening on ${port}`));
