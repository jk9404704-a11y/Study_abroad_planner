document.addEventListener('DOMContentLoaded', function () {
    const progressBar = document.querySelector('#ieltsProgress');
    const progressLabel = document.querySelector('#ieltsMessage');
    const visaIndicator = document.querySelector('#visaIndicator');
    const currencyResult = document.querySelector('#convertedAmount');
    const budgetOutput = document.querySelector('#budgetTotal');
    const budgetForm = document.querySelector('#budgetForm');
    const ieltsForm = document.querySelector('#ieltsForm');
    const currencyForm = document.querySelector('#currencyForm');

    function updateProgress(score) {
        if (!progressBar || !progressLabel) return;
        const percent = Math.min(Math.max((score / 9) * 100, 0), 100);
        progressBar.style.width = `${percent}%`;
        progressBar.setAttribute('aria-valuenow', percent.toFixed(0));
        if (percent >= 90) {
            progressLabel.textContent = 'Target Achieved';
        } else if (percent >= 60) {
            progressLabel.textContent = 'Excellent Progress';
        } else {
            progressLabel.textContent = 'Need More Practice';
        }
    }

    function updateVisaScore(score) {
        if (!visaIndicator) return;
        const circle = visaIndicator.querySelector('.indicator');
        const value = visaIndicator.querySelector('.progress-value');
        const clampScore = Math.min(Math.max(score, 0), 100);
        const circumference = 2 * Math.PI * 90;
        const dashOffset = circumference - (circumference * clampScore) / 100;
        circle.style.strokeDashoffset = dashOffset;
        value.textContent = `${clampScore}%`;
    }

    if (ieltsForm) {
        ieltsForm.addEventListener('submit', function (event) {
            event.preventDefault();
            const target = parseFloat(document.querySelector('#targetScore').value) || 0;
            const current = parseFloat(document.querySelector('#currentScore').value) || 0;
            const progress = Math.min(Math.max((current / target) * 100, 0), 100);
            updateProgress(progress);
        });
    }

    if (budgetForm) {
        budgetForm.addEventListener('submit', function (event) {
            event.preventDefault();
            const tuition = parseFloat(document.querySelector('#tuitionFee').value) || 0;
            const living = parseFloat(document.querySelector('#livingCost').value) || 0;
            const other = parseFloat(document.querySelector('#otherExpenses').value) || 0;
            if (!budgetOutput) return;
            const total = tuition + living + other;
            budgetOutput.textContent = `$${total.toLocaleString('en-US', {maximumFractionDigits:2})}`;
        });
    }

    if (currencyForm) {
        currencyForm.addEventListener('submit', function (event) {
            event.preventDefault();
            const amount = parseFloat(document.querySelector('#amountValue').value) || 0;
            const fromCurrency = document.querySelector('#fromCurrency').value;
            const toCurrency = document.querySelector('#toCurrency').value;
            const rates = {
                'USD': 1,
                'EUR': 0.92,
                'GBP': 0.81,
                'CAD': 1.34,
                'AUD': 1.53
            };
            const result = amount * (rates[toCurrency] / rates[fromCurrency] || 1);
            if (!currencyResult) return;
            currencyResult.textContent = `${amount.toFixed(2)} ${fromCurrency} = ${result.toFixed(2)} ${toCurrency}`;
        });
    }

    updateVisaScore(80);
});
