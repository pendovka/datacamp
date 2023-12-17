import extract
import transform
import load
import create_insights
import insights_export

if __name__ == "__main__":
    extract.main()
    transform.main()
    load.main()
    create_insights.main()
    insights_export.main()
