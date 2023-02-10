def kfre_4v_nonNA(in_ages, in_genders, in_egfrs, in_acrs) -> np.ndarray:
    """Takes numpy arrays and returns 2D numpy array with 2- and 5-year KFRE risks (non-NA calibrated).

    :param in_ages: Ages [year].
    :param in_genders: Genders - these are encoded as 0 (male) / 1 (female). TODO: Stringify.
    :param in_egfrs: Estimated glomerular filtration rates [mL/min/1.73m^2]. **Warning: This equation (KFRE) was built
            using the CKD-EPI equation  for estimated GFR.**
    :param in_acrs: Urinary albumin to creatinine ratios [mg/g]. **Warning: Inputs not assumed to be log-transformed.**

    Tangri N, Grams ME, Levey AS, Coresh J, Appel LJ, Astor BC, et al. Multinational Assessment of Accuracy of Equations
    for Predicting Risk of Kidney Failure: A Meta-analysis. JAMA. 2016 Jan 12;315(2):164.

    :return: 2D numpy array with float-type 2- and 5-year KFRE risks.
    """
    risks = np.empty(shape=(len(in_ages), 2), dtype="float")

    acrs = np.log(in_acrs, where=in_acrs > 1)

    risks[:, 0] = 1 - 0.9832 ** (
        np.exp(
            (-0.2201 * ((in_ages / 10) - 7.036)) + (0.2467 * ((in_genders ^ 1) - 0.5642))
            - (0.5567 * ((in_egfrs / 5) - 7.222)) + (0.4510 * (acrs - 5.137))
        )
    )
    risks[:, 1] = 1 - 0.9240 ** (
        np.exp(
            (-0.2201 * ((in_ages / 10) - 7.036)) + (0.2467 * ((in_genders ^ 1) - 0.5642))
            - (0.5567 * ((in_egfrs / 5) - 7.222)) + (0.4510 * (acrs - 5.137))
        )
    )

    return risks


def egfr_nejm(in_ages, in_genders, in_creats) -> np.ndarray:
    """Compute estimated glomerular filtration rates using NEJM equation (without race modifier).

    Inker LA, Eneanya ND, Coresh J, et al. New Creatinine- and Cystatin C–Based Equations to Estimate GFR without Race.
    New England Journal of Medicine. 2021;385(19):1737-1749. doi:10.1056/nejmoa2102953.

    :param in_ages: Ages [year].
    :param in_genders: Genders - these are encoded as 0 (male) / 1 (female). TODO: Stringify.
    :param in_creats: Creatinines [mg/dL].

    :return: 1D numpy array with computed NEJM eGFRs.
    """
    assert in_ages.shape == in_genders.shape == in_creats.shape

    ks = np.where(in_genders == 0, 0.9, 0.7)
    alphas = np.where(in_genders == 0, -0.302, -0.241)
    things = np.hstack([(in_creats / ks).reshape(-1, 1), np.full(len(in_ages), 1).reshape(-1, 1)])
    modifiers = np.where(in_genders == 0, 1, 1.012) * (0.9938 ** in_ages)

    egfrs = 142 * (np.min(things, axis=1) ** alphas) * (np.max(things, axis=1) ** -1.2) * modifiers

    return egfrs