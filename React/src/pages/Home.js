// components
import HomePageHeader from "../components/HomePageHeader"
import CategoryWrapper from "../components/CategoryWrapper"

// styles
import '../styles/GlobalStyles.css'

const Home = () => {
    return (
        <div class='page-container'>
            <HomePageHeader />
            <CategoryWrapper />
        </div>
    )
}

export default Home