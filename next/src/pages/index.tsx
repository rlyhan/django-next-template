import Layout from "../components/layout";
import { TestModel } from "@/types";

interface HomePageProps {
  objects: TestModel[];
}

function Home({ objects }: HomePageProps) {
  return (
    <Layout home>
      <div>Hello</div>
      {objects.map((object) => (
        <p>{object.name}</p>
      ))}
    </Layout>
  );
}

export async function getStaticProps() {
  const res = await fetch(process.env.API_URL);
  const objects = await res.json();

  return {
    props: {
      objects,
    },
  };
}

export default Home;
