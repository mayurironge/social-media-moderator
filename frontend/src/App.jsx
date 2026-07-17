import Header from "./components/Header";
import AnalyzerForm from "./components/AnalyzerForm";
import HistoryTable from "./components/HistoryTable";
import "./styles/App.css";

function App() {
  return (
    <div className="container">
      <Header />
      <AnalyzerForm />
      <HistoryTable />
    </div>
  );
}

export default App;