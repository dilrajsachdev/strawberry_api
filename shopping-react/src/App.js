import logo from "./logo.svg";
import "./App.css";
import { ApolloClient, InMemoryCache, ApolloProvider, useQuery, gql } from "@apollo/client";
import UserInfo from "./components/UserInfo";

const client = new ApolloClient({
    uri: "http://localhost:8000/graphql",
    cache: new InMemoryCache(),
});

client
    .query({
        query: gql`
            query Users {
                users {
                    username
                    email
                }
            }
        `,
    })
    .then((result) => console.log(result));

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

const App = () => (
    <ApolloProvider client={client}>
        <div
            style={{
                backgroundColor: "#00000008",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                height: "100vh",
                flexDirection: "column",
            }}
        >
            <h2>
                My first Apollo app{" "}
                <span role="img" aria-label="rocket">
                    🚀
                </span>
            </h2>

            <UserInfo />
        </div>
    </ApolloProvider>
);

export default App;
