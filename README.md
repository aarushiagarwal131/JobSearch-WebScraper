# Job Search Web Scraper

This Python script scrapes job listings from a website and filters them based on user-defined skills.

## Description

The Job Search Web Scraper is a Python script that utilizes the BeautifulSoup library to parse and extract job listings from a specific website. It then filters the jobs based on a skill that the user is not unfamiliar with and saves the relevant job details into individual text files.

The script is designed to run continuously, performing the job search and filtering at regular intervals.

## Getting Started

### Prerequisites

- Python 3.x
- BeautifulSoup (`pip install bs4`)
- Requests (`pip install requests`)

### Installation

1. Clone the repository:   git clone https://github.com/your-username/job-search-web-scraper.git
   
2. Install the required Python packages:  pip install -r requirements.txt

   
## Usage

1. Run the script: job.py

2. When prompted, enter a skill that you are not unfamiliar with.

3. The script will continuously search for job listings matching the provided skill. It will save the details of relevant jobs into separate text files within a `posts` directory.

## Customization

- You can modify the URL in the `find_jobs()` function in `job.py` to scrape job listings from a different website or with different search parameters.
- To adjust the time interval between job searches, modify the `time_wait` variable in the `if __name__ == '__main__':` section of `job.py`. The time is specified in minutes.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).



