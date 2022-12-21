import { useState } from "react";
import "./App.css";
import Avatar from "./avatar.png";

function App() {
  const [isLoading, setLoading] = useState(false);

  const [number, setNumber] = useState("");
  const [precisionType, setType] = useState("half");
  const [result, setResult] = useState({
    isShow: true,
    type: "single",
    number: "12.5",
    data: "01000001010010000000000000000000",
    mantissa: "10010000000000000000000",
    exponent: "10000010",
    sign: "0",
  });

  const handle = async () => {
    setLoading(true);
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ number: parseFloat(number), precisionType: precisionType }),
    };
    await fetch("https://api-ieee754.onrender.com/ieee754", requestOptions)
      .then((response) => response.json())
      .then((data) => {
        setResult({
          type: data.type,
          number: data.number,
          data: data.data,
          mantissa: data.mantissa,
          exponent: data.exponent,
          sign: data.sign,
          isShow: true,
        });
        setLoading(false);
      });
  };

  return (
    <div className="app">
      <div className="card">
        <a href="https://github.com/mehmethalis/ieee754-GUI" target={"_blank"} rel="noreferrer">
          <img src={Avatar} alt={"github"} className={"avatar"} />
        </a>
        <h4>Floating-Point Arithmetic | IEEE754</h4>
        <form>
          <label htmlFor="fname">Float Number</label>
          <input
            type="text"
            name="number"
            placeholder="Enter a number.."
            value={number}
            onChange={(e) =>
              !isNaN(parseInt(e.target.value[e.target.value.length - 1])) ||
              e.target.value[e.target.value.length - 1] === "." ||
              e.target.value === ""
                ? setNumber(e.target.value)
                : null
            }
          />

          <label>Precison Type</label>
          <select name="type" onChange={(e) => setType(e.target.value)} value={precisionType}>
            <option value="half">Half | 16-Bit</option>
            <option value="single">Single | 32-Bit</option>
            <option value="double">Double | 64-Bit</option>
            <option value="quadruple">Quadruple | 128-Bit</option>
            <option value="octuple">Octuple | 256-Bit</option>
          </select>

          <button type="button" onClick={() => handle()} disabled={!number}>
            {isLoading ? <div className="loader" /> : "CALCULATE"}
          </button>
        </form>
      </div>

      <div className="card-result">
        {result.isShow && (
          <>
            <div className="result-header">
              <span>
                <p>
                  Number : <b>{result.number}</b>
                </p>
                <p>
                  Precision Type: <b>{result.type}</b>
                </p>
              </span>
              <span className="legend">
                <div className="sign">
                  <div className="box" /> Sign Bit
                </div>
                <div className="exponent">
                  <div className="box" /> Exponent Bit
                </div>
                <div className="mantissa">
                  <div className="box" /> Mantissa Bit
                </div>
              </span>
            </div>
            <br />
            <br />

            <div className="sign">
              <div className="box">{result.sign}</div>
            </div>
            <div className="exponent">
              {result.exponent.split("").map((bit) => (
                <div className="box" key={Math.random()}>
                  {bit}
                </div>
              ))}
            </div>
            <div className="mantissa">
              {result.mantissa.split("").map((bit, index) => (
                <div className="box" key={Math.random()}>
                  {bit}
                </div>
              ))}
            </div>
          </>
        )}
      </div>
    </div>
  );
}

export default App;
