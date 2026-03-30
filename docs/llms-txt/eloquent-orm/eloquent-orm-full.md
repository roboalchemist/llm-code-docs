# Eloquent Orm Documentation

Source: https://laravel.com/docs/eloquent/llms-full.txt

---

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />

<title>Eloquent: Getting Started | Laravel 12.x - The clean stack for Artisans and agents</title>

    <link rel="canonical" href="https://laravel.com/docs/12.x/eloquent" />

<!-- Primary Meta Tags -->
<meta name="title" content="Eloquent: Getting Started | Laravel 12.x - The clean stack for Artisans and agents" />
<meta name="description" content="Laravel is a PHP web application framework with expressive, elegant syntax. We’ve already laid the foundation — freeing you to create without sweating the small things." />

<!-- Open Graph / Facebook -->
<meta property="og:type" content="website" />
<meta property="og:url" content="https://laravel.com/docs/12.x/eloquent" />
<meta property="og:title" content="Eloquent: Getting Started | Laravel 12.x - The clean stack for Artisans and agents" />
<meta property="og:description" content="Laravel is a PHP web application framework with expressive, elegant syntax. We’ve already laid the foundation — freeing you to create without sweating the small things." />
<meta
    property="og:image"
    content="https://laravel.com/images/og/laravel-docs-12.png"
/>
<!-- Twitter -->
<meta property="twitter:card" content="summary_large_image" />
<meta property="twitter:url" content="https://laravel.com/docs/12.x/eloquent" />
<meta property="twitter:title" content="Eloquent: Getting Started | Laravel 12.x - The clean stack for Artisans and agents" />
<meta property="twitter:description" content="Laravel is a PHP web application framework with expressive, elegant syntax. We’ve already laid the foundation — freeing you to create without sweating the small things." />
<meta
    property="twitter:image"
    content="https://laravel.com/images/og/laravel-docs-12.png"
/>
<!-- Favicon -->
<link rel="apple-touch-icon" sizes="180x180" href="/img/favicon/apple-touch-icon.png" />
<link rel="icon" type="image/png" sizes="32x32" href="/img/favicon/favicon-32x32.png" />
<link rel="icon" type="image/png" sizes="16x16" href="/img/favicon/favicon-16x16.png" />
<link rel="manifest" href="/img/favicon/site.webmanifest" />
<link rel="mask-icon" href="/img/favicon/safari-pinned-tab.svg" color="#ff2d20" />
<link rel="shortcut icon" href="/img/favicon/favicon.ico" />
<meta name="msapplication-TileColor" content="#ff2d20" />
<meta name="msapplication-config" content="/img/favicon/browserconfig.xml" />
<meta name="theme-color" content="#ffffff" />
<meta name="color-scheme" content="light" />

<link
    rel="preload"
    href="/fonts/instrumentSans/InstrumentSans-Regular.woff2"
    as="font"
    type="font/woff2"
    crossorigin="anonymous"
/>

<link rel="preconnect" href="https://E3MIRNPJH5-dsn.algolia.net" crossorigin />

<link rel="preload" as="style" href="https://laravel.com/build/assets/app-DbE-OJgB.css" /><link rel="modulepreload" href="https://laravel.com/build/assets/app-D_1jiBdE.js" /><link rel="modulepreload" href="https://laravel.com/build/assets/side-tabs-BYaOxqeh.js" /><link rel="modulepreload" href="https://laravel.com/build/assets/ai-boost-setup-BdU3OxRs.js" /><link rel="modulepreload" href="https://laravel.com/build/assets/module.esm-ClosvmSE.js" /><link rel="modulepreload" href="https://laravel.com/build/assets/mediaQuery-D0UE7bvU.js" /><link rel="modulepreload" href="https://laravel.com/build/assets/docs-B2804rWi.js" /><link rel="modulepreload" href="https://laravel.com/build/assets/theme-switcher-Qb8XCNxS.js" /><link rel="modulepreload" href="https://laravel.com/build/assets/index-CH_iu5NA.js" /><link rel="stylesheet" href="https://laravel.com/build/assets/app-DbE-OJgB.css" data-navigate-track="reload" /><script type="module" src="https://laravel.com/build/assets/app-D_1jiBdE.js" data-navigate-track="reload"></script><script type="module" src="https://laravel.com/build/assets/docs-B2804rWi.js" data-navigate-track="reload"></script>

    <!-- Fathom - beautiful, simple website analytics -->
    <script src="https://cdn.usefathom.com/script.js" data-site="DVMEKBYF" defer></script>
    <!-- / Fathom -->

    <!-- Clearbit -->
    <script
        async
        src="https://tag.clearbitscripts.com/v1/pk_97d2bf69f817feb07be42fcda1460119/tags.js"
        referrerpolicy="strict-origin-when-cross-origin"
    ></script>

<script>
    const alwaysLightMode =
        false;
    const alwaysDarkMode =
        false;
    const algolia_app_id = 'E3MIRNPJH5';
    const algolia_search_key = '1fa3a8fec06eb1858d6ca137211225c0';
    const version = '12.x';

    if (alwaysDarkMode) {
        document.documentElement.classList.add('dark');
        document.documentElement.setAttribute('data-theme', 'dark');
        document.documentElement.setAttribute('color-theme', 'dark');
    } else if (!alwaysLightMode) {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        const hasNoThemeOrIsSystemTheme = !localStorage.theme || localStorage.theme === 'system';

        if (localStorage.theme === 'dark' || (hasNoThemeOrIsSystemTheme && prefersDark)) {
            document.documentElement.classList.add('dark');
            document.documentElement.setAttribute('data-theme', 'dark');
            document.documentElement.setAttribute('color-theme', 'dark');
        }
    }
</script>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        // Set a CSS variable for the viewport width for the divider component
        document.documentElement.style.setProperty('--viewport-width', (document.body.clientWidth || 0) + 'px');
    });

    window.addEventListener(
        'resize',
        function () {
            document.documentElement.style.setProperty('--viewport-width', (document.body.clientWidth || 0) + 'px');
        },
        { passive: true },
    );
</script>

            </head>
    <body
        class=" bg-white font-sans text-neutral-900 antialiased dark:bg-neutral-900 dark:text-neutral-100"
    >
        <div class="w-full">
            <div class="">
                <div id="nav-trigger" class="absolute top-32 left-0"></div>

<nav
    class="sticky-nav docs-nav sticky top-0 z-99 mx-auto h-fit max-w-[1400px] !border-b-0 border-l !border-neutral-200 bg-white px-4 py-8 transition-transform duration-300 xl:px-16 dark:!border-neutral-700 dark:bg-neutral-900"
>
    <div class="grid grid-cols-12 gap-4 lg:gap-6 xl:gap-x-10 relative h-full items-center overflow-hidden">
    <ul class="col-span-3 flex items-start space-x-8 font-medium">
            <li class="mr-18 w-20 text-laravel-red transition-transform duration-300 ease-in-out" id="nav-left">
                <a href="https://laravel.com" class="flex aspect-[80/23] w-20 items-center">
                    <svg class="h-full w-full"
    width="1280"
    height="308"
    viewBox="0 0 1280 308"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
>
    <path
        d="M50.2753 0H0V308.689H144.713V263.27H50.2753V0Z"
        fill="currentColor"
    />
    <path
        d="M322.209 130.973C315.796 120.684 306.688 112.602 294.883 106.718C283.081 100.84 271.201 97.8969 259.253 97.8969C243.798 97.8969 229.665 100.764 216.843 106.496C204.014 112.228 193.015 120.099 183.834 130.091C174.654 140.088 167.51 151.628 162.412 164.706C157.308 177.792 154.761 191.54 154.761 205.94C154.761 220.645 157.308 234.457 162.412 247.39C167.508 260.332 174.652 271.796 183.834 281.788C193.015 291.785 204.017 299.647 216.843 305.379C229.665 311.111 243.798 313.978 259.253 313.978C271.201 313.978 283.081 311.038 294.883 305.159C306.688 299.282 315.796 291.197 322.209 280.904V308.685H369.865V103.186H322.209V130.973ZM317.837 231.076C314.922 239.016 310.841 245.925 305.598 251.804C300.35 257.687 294.009 262.389 286.579 265.917C279.146 269.445 270.905 271.208 261.875 271.208C252.837 271.208 244.676 269.445 237.391 265.917C230.104 262.389 223.839 257.687 218.593 251.804C213.345 245.925 209.335 239.016 206.57 231.076C203.794 223.138 202.417 214.759 202.417 205.942C202.417 197.12 203.794 188.742 206.57 180.804C209.335 172.866 213.345 165.961 218.593 160.078C223.839 154.201 230.102 149.493 237.391 145.965C244.676 142.437 252.837 140.674 261.875 140.674C270.908 140.674 279.146 142.437 286.579 145.965C294.009 149.493 300.35 154.199 305.598 160.078C310.844 165.961 314.922 172.866 317.837 180.804C320.748 188.742 322.209 197.12 322.209 205.942C322.209 214.759 320.748 223.138 317.837 231.076Z"
        fill="currentColor"
    />
    <path
        d="M709.568 130.973C703.155 120.684 694.047 112.602 682.242 106.718C670.44 100.84 658.56 97.8969 646.612 97.8969C631.157 97.8969 617.024 100.764 604.202 106.496C591.373 112.228 580.374 120.099 571.193 130.091C562.013 140.088 554.869 151.628 549.771 164.706C544.666 177.792 542.12 191.54 542.12 205.94C542.12 220.645 544.666 234.457 549.771 247.39C554.867 260.332 562.01 271.796 571.193 281.788C580.374 291.785 591.375 299.647 604.202 305.379C617.024 311.111 631.157 313.978 646.612 313.978C658.56 313.978 670.44 311.038 682.242 305.159C694.047 299.282 703.155 291.197 709.568 280.904V308.685H757.224V103.186H709.568V130.973ZM705.198 231.076C702.283 239.016 698.202 245.925 692.959 251.804C687.711 257.687 681.37 262.389 673.94 265.917C666.507 269.445 658.266 271.208 649.236 271.208C640.198 271.208 632.037 269.445 624.752 265.917C617.465 262.389 611.2 257.687 605.954 251.804C600.706 245.925 596.696 239.016 593.931 231.076C591.155 223.138 589.778 214.759 589.778 205.942C589.778 197.12 591.155 188.742 593.931 180.804C596.696 172.866 600.706 165.961 605.954 160.078C611.2 154.201 617.463 149.493 624.752 145.965C632.037 142.437 640.198 140.674 649.236 140.674C658.269 140.674 666.507 142.437 673.94 145.965C681.37 149.493 687.711 154.199 692.959 160.078C698.205 165.961 702.283 172.866 705.198 180.804C708.109 188.742 709.57 197.12 709.57 205.942C709.568 214.759 708.107 223.138 705.198 231.076Z"
        fill="currentColor"
    />
    <path
        d="M1280 1.12315e-05H1232.35V308.689H1280V1.12315e-05Z"
        fill="currentColor"
    />
    <path
        d="M407.466 308.689H455.117V150.486H536.876V103.192H407.466V308.689Z"
        fill="currentColor"
    />
    <path
        d="M948.281 103.192L888.386 260.557L828.489 103.192H780.224L858.441 308.689H918.331L996.546 103.192H948.281Z"
        fill="currentColor"
    />
    <path
        d="M1100.48 97.908C1042.13 97.908 995.937 146.279 995.937 205.944C995.937 271.9 1040.64 313.98 1106.59 313.98C1143.5 313.98 1167.06 299.745 1195.85 268.746L1163.66 243.621C1163.64 243.646 1139.36 275.802 1103.1 275.802C1060.96 275.802 1043.22 241.533 1043.22 223.803H1201.32C1209.62 155.913 1165.37 97.908 1100.48 97.908ZM1043.35 188.085C1043.71 184.13 1049.2 136.086 1100.1 136.086C1151.01 136.086 1157.19 184.123 1157.55 188.085H1043.35Z"
        fill="currentColor"
    />
</svg>                    <span class="sr-only">Home</span>
                </a>
            </li>
        </ul>

        <div
            class="absolute -top-1 right-9 flex cursor-pointer items-center rounded-xs p-2 text-sand-light-9-alpha-45 lg:relative lg:top-auto lg:right-auto lg:col-span-6 lg:w-full lg:bg-sand-light-3 lg:hover:bg-sand-light-4 dark:text-sand-dark-11 lg:dark:bg-sand-dark-5 lg:dark:hover:bg-sand-dark-4"
        >
            <svg class="h-6 w-6 shrink-0 lg:mr-2 lg:h-5 lg:w-5"
    width="20"
    height="20"
    viewBox="0 0 20 20"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
>
    <g>
        <path
            d="M15.8333 15.8333L13.0523 13.0524M13.0523 13.0524C13.9943 12.1104 14.5769 10.8092 14.5769 9.3718C14.5769 6.49708 12.2465 4.16667 9.37176 4.16667C6.49704 4.16667 4.16663 6.49708 4.16663 9.3718C4.16663 12.2465 6.49704 14.5769 9.37176 14.5769C10.8091 14.5769 12.1104 13.9943 13.0523 13.0524Z"
            stroke="currentColor"
            stroke-width="1.5"
            stroke-linecap="round"
            stroke-linejoin="round"
        />
    </g>
</svg>            <div class="grow">
                <div
                    id="docsearch"
                    class="absolute inset-0 bg-transparent text-base text-sand-light-9-alpha-45/70 *:absolute *:inset-0 lg:*:px-9 lg:*:py-1.5 dark:text-sand-dark-10"
                ></div>
            </div>
            <span
                class="mr-1.5 ml-2 hidden shrink-0 text-sm font-medium text-sand-light-9 lg:block dark:text-sand-dark-10"
            >
                ⌘K
            </span>
        </div>

        <div class="col-span-9 flex items-center justify-end gap-4 lg:col-span-3 dark:text-sand-dark-12">
            <select
    x-data
    aria-label="Laravel version"
    @change="window.location = $event.target.value"
    class="hidden border-0 bg-sand-light-1 px-3 py-1.5 text-sm whitespace-nowrap lg:block dark:bg-sand-dark-1"
>
            <option  value="https://laravel.com/docs/master/eloquent">
            Version Master
        </option>
            <option selected value="https://laravel.com/docs/12.x/eloquent">
            Version 12.x
        </option>
            <option  value="https://laravel.com/docs/11.x/eloquent">
            Version 11.x
        </option>
            <option  value="https://laravel.com/docs/10.x/eloquent">
            Version 10.x
        </option>
            <option  value="https://laravel.com/docs/9.x/eloquent">
            Version 9.x
        </option>
            <option  value="https://laravel.com/docs/8.x/eloquent">
            Version 8.x
        </option>
            <option  value="https://laravel.com/docs/7.x/eloquent">
            Version 7.x
        </option>
            <option  value="https://laravel.com/docs/6.x/eloquent">
            Version 6.x
        </option>
            <option  value="https://laravel.com/docs/5.8/eloquent">
            Version 5.8
        </option>
            <option  value="https://laravel.com/docs/5.7/eloquent">
            Version 5.7
        </option>
            <option  value="https://laravel.com/docs/5.6/eloquent">
            Version 5.6
        </option>
            <option  value="https://laravel.com/docs/5.5/eloquent">
            Version 5.5
        </option>
            <option  value="https://laravel.com/docs/5.4/eloquent">
            Version 5.4
        </option>
            <option  value="https://laravel.com/docs/5.3/eloquent">
            Version 5.3
        </option>
            <option  value="https://laravel.com/docs/5.2/eloquent">
            Version 5.2
        </option>
            <option  value="https://laravel.com/docs/5.1/eloquent">
            Version 5.1
        </option>
            <option  value="https://laravel.com/docs/5.0/eloquent">
            Version 5.0
        </option>
            <option  value="https://laravel.com/docs/4.2/eloquent">
            Version 4.2
        </option>
    </select>

            <select
    x-data
    aria-label="Laravel version"
    @change="window.location = $event.target.value"
    class="border-0 bg-sand-light-1 px-3 py-1.5 text-sm whitespace-nowrap lg:hidden dark:bg-sand-dark-1"
>
            <option  value="https://laravel.com/docs/master/eloquent">
            vMaster
        </option>
            <option selected value="https://laravel.com/docs/12.x/eloquent">
            v12.x
        </option>
            <option  value="https://laravel.com/docs/11.x/eloquent">
            v11.x
        </option>
            <option  value="https://laravel.com/docs/10.x/eloquent">
            v10.x
        </option>
            <option  value="https://laravel.com/docs/9.x/eloquent">
            v9.x
        </option>
            <option  value="https://laravel.com/docs/8.x/eloquent">
            v8.x
        </option>
            <option  value="https://laravel.com/docs/7.x/eloquent">
            v7.x
        </option>
            <option  value="https://laravel.com/docs/6.x/eloquent">
            v6.x
        </option>
            <option  value="https://laravel.com/docs/5.8/eloquent">
            v5.8
        </option>
            <option  value="https://laravel.com/docs/5.7/eloquent">
            v5.7
        </option>
            <option  value="https://laravel.com/docs/5.6/eloquent">
            v5.6
        </option>
            <option  value="https://laravel.com/docs/5.5/eloquent">
            v5.5
        </option>
            <option  value="https://laravel.com/docs/5.4/eloquent">
            v5.4
        </option>
            <option  value="https://laravel.com/docs/5.3/eloquent">
            v5.3
        </option>
            <option  value="https://laravel.com/docs/5.2/eloquent">
            v5.2
        </option>
            <option  value="https://laravel.com/docs/5.1/eloquent">
            v5.1
        </option>
            <option  value="https://laravel.com/docs/5.0/eloquent">
            v5.0
        </option>
            <option  value="https://laravel.com/docs/4.2/eloquent">
            v4.2
        </option>
    </select>

            <div class="hidden lg:block">
                <div
    class="flex items-center size-8 group"
    x-data="themeSwitcher"
    x-on:switch-theme.window="saveAndUpdate($event.detail)"
>
    <button
        id="header__sun"
        @click="toSystemMode"
        title="Switch to system theme"
        class="focus:shadow-outline flex size-8 cursor-default items-center justify-center text-sand-light-12 transition duration-100 group-hover:text-sand-light-10 focus:outline-none dark:text-sand-dark-12 dark:group-hover:text-sand-dark-10"
    >
        <svg class="size-6" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.0002 3.29071V1.76746M5.8418 18.1585L4.7647 19.2356M12.0002 22.2326V20.7093M19.2357 4.76456L18.1586 5.84166M20.7095 12H22.2327M18.1586 18.1584L19.2357 19.2355M1.76758 12H3.29083M4.76462 4.7645L5.84173 5.8416M15.7123 8.2877C17.7626 10.338 17.7626 13.6621 15.7123 15.7123C13.6621 17.7626 10.338 17.7626 8.2877 15.7123C6.23745 13.6621 6.23745 10.338 8.2877 8.2877C10.338 6.23745 13.6621 6.23745 15.7123 8.2877Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="square" stroke-linejoin="round"/>
</svg>    </button>
    <button
        id="header__moon"
        @click="toLightMode"
        title="Switch to light mode"
        class="focus:shadow-outline flex size-8 cursor-default items-center justify-center text-sand-light-12 transition duration-100 group-hover:text-sand-light-10 focus:outline-none dark:text-sand-dark-12 dark:group-hover:text-sand-dark-10"
    >
        <svg class="size-6" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M20.2496 14.1987C19.5326 14.3951 18.7782 14.5 18 14.5C13.3056 14.5 9.5 10.6944 9.5 5.99999C9.5 5.22185 9.60487 4.4674 9.80124 3.75043C6.15452 4.72095 3.46777 8.04578 3.46777 11.9981C3.46777 16.7114 7.28864 20.5323 12.0019 20.5323C15.9543 20.5323 19.2791 17.8455 20.2496 14.1987ZM20.5196 12.5328C19.7378 12.8346 18.8882 13 18 13C14.134 13 11 9.86598 11 5.99999C11 5.11181 11.1654 4.26226 11.4671 3.48047C11.6142 3.09951 11.7935 2.73464 12.0019 2.38923C12.0888 2.24526 12.1807 2.10466 12.2774 1.9677C12.1858 1.96523 12.094 1.96399 12.0019 1.96399C11.4758 1.96399 10.9592 2.00448 10.455 2.0825C5.64774 2.8264 1.96777 6.98251 1.96777 11.9981C1.96777 17.5398 6.46021 22.0323 12.0019 22.0323C17.0176 22.0323 21.1737 18.3523 21.9176 13.545C21.9956 13.0408 22.0361 12.5242 22.0361 11.9981C22.0361 11.906 22.0348 11.8141 22.0323 11.7226C21.8953 11.8193 21.7547 11.9112 21.6107 11.9981C21.2653 12.2065 20.9005 12.3858 20.5196 12.5328Z" fill="currentColor"/>
<path d="M16.3333 5.33333L17.5 3L18.6667 5.33333L21 6.5L18.6667 7.66667L17.5 10L16.3333 7.66667L14 6.5L16.3333 5.33333Z" fill="currentColor"/>
</svg>    </button>
    <button
        id="header__indeterminate"
        @click="toDarkMode"
        title="Switch to dark mode"
        class="focus:shadow-outline flex size-8 cursor-default items-center justify-center text-sand-light-12 transition duration-100 group-hover:text-sand-light-10 focus:outline-none dark:text-sand-dark-12 dark:group-hover:text-sand-dark-10"
    >
        <svg class="size-6 dark:hidden" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M20.5 12C20.5 16.6944 16.6944 20.5 12 20.5V3.5C16.6944 3.5 20.5 7.30558 20.5 12ZM12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" fill="currentColor" />
</svg>        <svg class="hidden size-6 dark:block" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M20.5 12C20.5 16.6944 16.6944 20.5 12 20.5V3.5C16.6944 3.5 20.5 7.30558 20.5 12ZM12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" fill="currentColor"/>
</svg>    </button>
</div>
            </div>

            <button popovertarget="docs-nav-mobile" class="ml-13 cursor-pointer lg:hidden">
                <svg class="hamburger-menu h-6 w-6 text-sand-light-9"
    width="24"
    height="24"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
>
    <path
        d="M2.75 7.25H21.25M2.75 16.75H21.25"
        stroke="currentColor"
        stroke-width="1.5"
        stroke-linecap="square"
    />
</svg>                <svg class="close-menu h-6 w-6 text-sand-light-9"
    width="24"
    height="24"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
>
    <path
        d="M4.75 4.75L19.25 19.25M19.25 4.75L4.75 19.25"
        stroke="currentColor"
        stroke-width="1.5"
        stroke-linecap="square"
    />
</svg>            </button>
        </div>
</div>
</nav>

<div
    popover
    id="docs-nav-mobile"
    class="main-nav-popover fixed w-full bg-transparent"
    style="top: var(--mobile-menu-top, 4rem)"
>
    <div
        class="docs_sidebar relative h-[calc(100dvh-5.5rem)] overflow-auto border-b bg-sand-light-1 px-5 py-8 dark:bg-sand-dark-1"
    >
        <div class="absolute top-5 right-8">
            <div
    class="flex items-center size-8 group"
    x-data="themeSwitcher"
    x-on:switch-theme.window="saveAndUpdate($event.detail)"
>
    <button
        id="header__sun"
        @click="toSystemMode"
        title="Switch to system theme"
        class="focus:shadow-outline flex size-8 cursor-default items-center justify-center text-sand-light-12 transition duration-100 group-hover:text-sand-light-10 focus:outline-none dark:text-sand-dark-12 dark:group-hover:text-sand-dark-10"
    >
        <svg class="size-6" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.0002 3.29071V1.76746M5.8418 18.1585L4.7647 19.2356M12.0002 22.2326V20.7093M19.2357 4.76456L18.1586 5.84166M20.7095 12H22.2327M18.1586 18.1584L19.2357 19.2355M1.76758 12H3.29083M4.76462 4.7645L5.84173 5.8416M15.7123 8.2877C17.7626 10.338 17.7626 13.6621 15.7123 15.7123C13.6621 17.7626 10.338 17.7626 8.2877 15.7123C6.23745 13.6621 6.23745 10.338 8.2877 8.2877C10.338 6.23745 13.6621 6.23745 15.7123 8.2877Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="square" stroke-linejoin="round"/>
</svg>    </button>
    <button
        id="header__moon"
        @click="toLightMode"
        title="Switch to light mode"
        class="focus:shadow-outline flex size-8 cursor-default items-center justify-center text-sand-light-12 transition duration-100 group-hover:text-sand-light-10 focus:outline-none dark:text-sand-dark-12 dark:group-hover:text-sand-dark-10"
    >
        <svg class="size-6" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M20.2496 14.1987C19.5326 14.3951 18.7782 14.5 18 14.5C13.3056 14.5 9.5 10.6944 9.5 5.99999C9.5 5.22185 9.60487 4.4674 9.80124 3.75043C6.15452 4.72095 3.46777 8.04578 3.46777 11.9981C3.46777 16.7114 7.28864 20.5323 12.0019 20.5323C15.9543 20.5323 19.2791 17.8455 20.2496 14.1987ZM20.5196 12.5328C19.7378 12.8346 18.8882 13 18 13C14.134 13 11 9.86598 11 5.99999C11 5.11181 11.1654 4.26226 11.4671 3.48047C11.6142 3.09951 11.7935 2.73464 12.0019 2.38923C12.0888 2.24526 12.1807 2.10466 12.2774 1.9677C12.1858 1.96523 12.094 1.96399 12.0019 1.96399C11.4758 1.96399 10.9592 2.00448 10.455 2.0825C5.64774 2.8264 1.96777 6.98251 1.96777 11.9981C1.96777 17.5398 6.46021 22.0323 12.0019 22.0323C17.0176 22.0323 21.1737 18.3523 21.9176 13.545C21.9956 13.0408 22.0361 12.5242 22.0361 11.9981C22.0361 11.906 22.0348 11.8141 22.0323 11.7226C21.8953 11.8193 21.7547 11.9112 21.6107 11.9981C21.2653 12.2065 20.9005 12.3858 20.5196 12.5328Z" fill="currentColor"/>
<path d="M16.3333 5.33333L17.5 3L18.6667 5.33333L21 6.5L18.6667 7.66667L17.5 10L16.3333 7.66667L14 6.5L16.3333 5.33333Z" fill="currentColor"/>
</svg>    </button>
    <button
        id="header__indeterminate"
        @click="toDarkMode"
        title="Switch to dark mode"
        class="focus:shadow-outline flex size-8 cursor-default items-center justify-center text-sand-light-12 transition duration-100 group-hover:text-sand-light-10 focus:outline-none dark:text-sand-dark-12 dark:group-hover:text-sand-dark-10"
    >
        <svg class="size-6 dark:hidden" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M20.5 12C20.5 16.6944 16.6944 20.5 12 20.5V3.5C16.6944 3.5 20.5 7.30558 20.5 12ZM12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" fill="currentColor" />
</svg>        <svg class="hidden size-6 dark:block" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M20.5 12C20.5 16.6944 16.6944 20.5 12 20.5V3.5C16.6944 3.5 20.5 7.30558 20.5 12ZM12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" fill="currentColor"/>
</svg>    </button>
</div>
        </div>

        <ul>
<li>
<h2>Prologue</h2>
<ul>
<li><a href="/docs/12.x/releases">Release Notes</a></li>
<li><a href="/docs/12.x/upgrade">Upgrade Guide</a></li>
<li><a href="/docs/12.x/contributions">Contribution Guide</a></li>
</ul>
</li>
<li>
<h2>Getting Started</h2>
<ul>
<li><a href="/docs/12.x/installation">Installation</a></li>
<li><a href="/docs/12.x/configuration">Configuration</a></li>
<li><a href="/docs/12.x/ai">Agentic Development</a></li>
<li><a href="/docs/12.x/structure">Directory Structure</a></li>
<li><a href="/docs/12.x/frontend">Frontend</a></li>
<li><a href="/docs/12.x/starter-kits">Starter Kits</a></li>
<li><a href="/docs/12.x/deployment">Deployment</a></li>
</ul>
</li>
<li>
<h2>Architecture Concepts</h2>
<ul>
<li><a href="/docs/12.x/lifecycle">Request Lifecycle</a></li>
<li><a href="/docs/12.x/container">Service Container</a></li>
<li><a href="/docs/12.x/providers">Service Providers</a></li>
<li><a href="/docs/12.x/facades">Facades</a></li>
</ul>
</li>
<li>
<h2>The Basics</h2>
<ul>
<li><a href="/docs/12.x/routing">Routing</a></li>
<li><a href="/docs/12.x/middleware">Middleware</a></li>
<li><a href="/docs/12.x/csrf">CSRF Protection</a></li>
<li><a href="/docs/12.x/controllers">Controllers</a></li>
<li><a href="/docs/12.x/requests">Requests</a></li>
<li><a href="/docs/12.x/responses">Responses</a></li>
<li><a href="/docs/12.x/views">Views</a></li>
<li><a href="/docs/12.x/blade">Blade Templates</a></li>
<li><a href="/docs/12.x/vite">Asset Bundling</a></li>
<li><a href="/docs/12.x/urls">URL Generation</a></li>
<li><a href="/docs/12.x/session">Session</a></li>
<li><a href="/docs/12.x/validation">Validation</a></li>
<li><a href="/docs/12.x/errors">Error Handling</a></li>
<li><a href="/docs/12.x/logging">Logging</a></li>
</ul>
</li>
<li>
<h2>Digging Deeper</h2>
<ul>
<li><a href="/docs/12.x/artisan">Artisan Console</a></li>
<li><a href="/docs/12.x/broadcasting">Broadcasting</a></li>
<li><a href="/docs/12.x/cache">Cache</a></li>
<li><a href="/docs/12.x/collections">Collections</a></li>
<li><a href="/docs/12.x/concurrency">Concurrency</a></li>
<li><a href="/docs/12.x/context">Context</a></li>
<li><a href="/docs/12.x/contracts">Contracts</a></li>
<li><a href="/docs/12.x/events">Events</a></li>
<li><a href="/docs/12.x/filesystem">File Storage</a></li>
<li><a href="/docs/12.x/helpers">Helpers</a></li>
<li><a href="/docs/12.x/http-client">HTTP Client</a></li>
<li><a href="/docs/12.x/localization">Localization</a></li>
<li><a href="/docs/12.x/mail">Mail</a></li>
<li><a href="/docs/12.x/notifications">Notifications</a></li>
<li><a href="/docs/12.x/packages">Package Development</a></li>
<li><a href="/docs/12.x/processes">Processes</a></li>
<li><a href="/docs/12.x/queues">Queues</a></li>
<li><a href="/docs/12.x/rate-limiting">Rate Limiting</a></li>
<li><a href="/docs/12.x/search">Search</a></li>
<li><a href="/docs/12.x/strings">Strings</a></li>
<li><a href="/docs/12.x/scheduling">Task Scheduling</a></li>
</ul>
</li>
<li>
<h2>Security</h2>
<ul>
<li><a href="/docs/12.x/authentication">Authentication</a></li>
<li><a href="/docs/12.x/authorization">Authorization</a></li>
<li><a href="/docs/12.x/verification">Email Verification</a></li>
<li><a href="/docs/12.x/encryption">Encryption</a></li>
<li><a href="/docs/12.x/hashing">Hashing</a></li>
<li><a href="/docs/12.x/passwords">Password Reset</a></li>
</ul>
</li>
<li>
<h2>Database</h2>
<ul>
<li><a href="/docs/12.x/database">Getting Started</a></li>
<li><a href="/docs/12.x/queries">Query Builder</a></li>
<li><a href="/docs/12.x/pagination">Pagination</a></li>
<li><a href="/docs/12.x/migrations">Migrations</a></li>
<li><a href="/docs/12.x/seeding">Seeding</a></li>
<li><a href="/docs/12.x/redis">Redis</a></li>
<li><a href="/docs/12.x/mongodb">MongoDB</a></li>
</ul>
</li>
<li class="sub--on">
<h2>Eloquent ORM</h2>
<ul>
<li class="active"><a href="/docs/12.x/eloquent">Getting Started</a></li>
<li><a href="/docs/12.x/eloquent-relationships">Relationships</a></li>
<li><a href="/docs/12.x/eloquent-collections">Collections</a></li>
<li><a href="/docs/12.x/eloquent-mutators">Mutators / Casts</a></li>
<li><a href="/docs/12.x/eloquent-resources">API Resources</a></li>
<li><a href="/docs/12.x/eloquent-serialization">Serialization</a></li>
<li><a href="/docs/12.x/eloquent-factories">Factories</a></li>
</ul>
</li>
<li>
<h2>AI</h2>
<ul>
<li><a href="/docs/12.x/ai-sdk">AI SDK</a></li>
<li><a href="/docs/12.x/mcp">MCP</a></li>
<li><a href="/docs/12.x/boost">Boost</a></li>
</ul>
</li>
<li>
<h2>Testing</h2>
<ul>
<li><a href="/docs/12.x/testing">Getting Started</a></li>
<li><a href="/docs/12.x/http-tests">HTTP Tests</a></li>
<li><a href="/docs/12.x/console-tests">Console Tests</a></li>
<li><a href="/docs/12.x/dusk">Browser Tests</a></li>
<li><a href="/docs/12.x/database-testing">Database</a></li>
<li><a href="/docs/12.x/mocking">Mocking</a></li>
</ul>
</li>
<li>
<h2>Packages</h2>
<ul>
<li><a href="/docs/12.x/billing">Cashier (Stripe)</a></li>
<li><a href="/docs/12.x/cashier-paddle">Cashier (Paddle)</a></li>
<li><a href="/docs/12.x/dusk">Dusk</a></li>
<li><a href="/docs/12.x/envoy">Envoy</a></li>
<li><a href="/docs/12.x/fortify">Fortify</a></li>
<li><a href="/docs/12.x/folio">Folio</a></li>
<li><a href="/docs/12.x/homestead">Homestead</a></li>
<li><a href="/docs/12.x/horizon">Horizon</a></li>
<li><a href="/docs/12.x/mix">Mix</a></li>
<li><a href="/docs/12.x/octane">Octane</a></li>
<li><a href="/docs/12.x/passport">Passport</a></li>
<li><a href="/docs/12.x/pennant">Pennant</a></li>
<li><a href="/docs/12.x/pint">Pint</a></li>
<li><a href="/docs/12.x/precognition">Precognition</a></li>
<li><a href="/docs/12.x/prompts">Prompts</a></li>
<li><a href="/docs/12.x/pulse">Pulse</a></li>
<li><a href="/docs/12.x/reverb">Reverb</a></li>
<li><a href="/docs/12.x/sail">Sail</a></li>
<li><a href="/docs/12.x/sanctum">Sanctum</a></li>
<li><a href="/docs/12.x/scout">Scout</a></li>
<li><a href="/docs/12.x/socialite">Socialite</a></li>
<li><a href="/docs/12.x/telescope">Telescope</a></li>
<li><a href="/docs/12.x/valet">Valet</a></li>
</ul>
</li>
<li><a href="https://api.laravel.com/docs/12.x">API Documentation</a></li>
<li><a href="/docs/changelog">Changelog</a></li></ul>

    </div>
</div>

                <div class="mx-auto max-w-[1400px] border-l border-neutral-200 dark:border-neutral-700">
        <div class="px-4 xl:px-16">
            <a
    id="skip-to-content-link"
    href="#main-content"
    class="absolute top-3 left-3 bg-gray-100 px-4 py-2 text-gray-700 shadow-xl"
>
    Skip to content
</a>

            <div class="grid grid-cols-12 gap-4 lg:gap-6 xl:gap-x-10 px-6 pt-10 lg:px-0" id="docsScreen">
    <aside class="relative col-span-3 lg:pb-6">
                    <div class="sticky top-22 bottom-0 left-0 z-20 hidden lg:block">
                        <div
                            class="sticky-side-nav clean-scrollbar relative -ml-16 flex max-h-screen flex-1 flex-col overflow-auto pl-16"
                        >
                            <nav id="indexed-nav" class="hidden lg:block">
                                <div class="docs_sidebar">
                                    <ul>
<li>
<h2>Prologue</h2>
<ul>
<li><a href="/docs/12.x/releases">Release Notes</a></li>
<li><a href="/docs/12.x/upgrade">Upgrade Guide</a></li>
<li><a href="/docs/12.x/contributions">Contribution Guide</a></li>
</ul>
</li>
<li>
<h2>Getting Started</h2>
<ul>
<li><a href="/docs/12.x/installation">Installation</a></li>
<li><a href="/docs/12.x/configuration">Configuration</a></li>
<li><a href="/docs/12.x/ai">Agentic Development</a></li>
<li><a href="/docs/12.x/structure">Directory Structure</a></li>
<li><a href="/docs/12.x/frontend">Frontend</a></li>
<li><a href="/docs/12.x/starter-kits">Starter Kits</a></li>
<li><a href="/docs/12.x/deployment">Deployment</a></li>
</ul>
</li>
<li>
<h2>Architecture Concepts</h2>
<ul>
<li><a href="/docs/12.x/lifecycle">Request Lifecycle</a></li>
<li><a href="/docs/12.x/container">Service Container</a></li>
<li><a href="/docs/12.x/providers">Service Providers</a></li>
<li><a href="/docs/12.x/facades">Facades</a></li>
</ul>
</li>
<li>
<h2>The Basics</h2>
<ul>
<li><a href="/docs/12.x/routing">Routing</a></li>
<li><a href="/docs/12.x/middleware">Middleware</a></li>
<li><a href="/docs/12.x/csrf">CSRF Protection</a></li>
<li><a href="/docs/12.x/controllers">Controllers</a></li>
<li><a href="/docs/12.x/requests">Requests</a></li>
<li><a href="/docs/12.x/responses">Responses</a></li>
<li><a href="/docs/12.x/views">Views</a></li>
<li><a href="/docs/12.x/blade">Blade Templates</a></li>
<li><a href="/docs/12.x/vite">Asset Bundling</a></li>
<li><a href="/docs/12.x/urls">URL Generation</a></li>
<li><a href="/docs/12.x/session">Session</a></li>
<li><a href="/docs/12.x/validation">Validation</a></li>
<li><a href="/docs/12.x/errors">Error Handling</a></li>
<li><a href="/docs/12.x/logging">Logging</a></li>
</ul>
</li>
<li>
<h2>Digging Deeper</h2>
<ul>
<li><a href="/docs/12.x/artisan">Artisan Console</a></li>
<li><a href="/docs/12.x/broadcasting">Broadcasting</a></li>
<li><a href="/docs/12.x/cache">Cache</a></li>
<li><a href="/docs/12.x/collections">Collections</a></li>
<li><a href="/docs/12.x/concurrency">Concurrency</a></li>
<li><a href="/docs/12.x/context">Context</a></li>
<li><a href="/docs/12.x/contracts">Contracts</a></li>
<li><a href="/docs/12.x/events">Events</a></li>
<li><a href="/docs/12.x/filesystem">File Storage</a></li>
<li><a href="/docs/12.x/helpers">Helpers</a></li>
<li><a href="/docs/12.x/http-client">HTTP Client</a></li>
<li><a href="/docs/12.x/localization">Localization</a></li>
<li><a href="/docs/12.x/mail">Mail</a></li>
<li><a href="/docs/12.x/notifications">Notifications</a></li>
<li><a href="/docs/12.x/packages">Package Development</a></li>
<li><a href="/docs/12.x/processes">Processes</a></li>
<li><a href="/docs/12.x/queues">Queues</a></li>
<li><a href="/docs/12.x/rate-limiting">Rate Limiting</a></li>
<li><a href="/docs/12.x/search">Search</a></li>
<li><a href="/docs/12.x/strings">Strings</a></li>
<li><a href="/docs/12.x/scheduling">Task Scheduling</a></li>
</ul>
</li>
<li>
<h2>Security</h2>
<ul>
<li><a href="/docs/12.x/authentication">Authentication</a></li>
<li><a href="/docs/12.x/authorization">Authorization</a></li>
<li><a href="/docs/12.x/verification">Email Verification</a></li>
<li><a href="/docs/12.x/encryption">Encryption</a></li>
<li><a href="/docs/12.x/hashing">Hashing</a></li>
<li><a href="/docs/12.x/passwords">Password Reset</a></li>
</ul>
</li>
<li>
<h2>Database</h2>
<ul>
<li><a href="/docs/12.x/database">Getting Started</a></li>
<li><a href="/docs/12.x/queries">Query Builder</a></li>
<li><a href="/docs/12.x/pagination">Pagination</a></li>
<li><a href="/docs/12.x/migrations">Migrations</a></li>
<li><a href="/docs/12.x/seeding">Seeding</a></li>
<li><a href="/docs/12.x/redis">Redis</a></li>
<li><a href="/docs/12.x/mongodb">MongoDB</a></li>
</ul>
</li>
<li class="sub--on">
<h2>Eloquent ORM</h2>
<ul>
<li class="active"><a href="/docs/12.x/eloquent">Getting Started</a></li>
<li><a href="/docs/12.x/eloquent-relationships">Relationships</a></li>
<li><a href="/docs/12.x/eloquent-collections">Collections</a></li>
<li><a href="/docs/12.x/eloquent-mutators">Mutators / Casts</a></li>
<li><a href="/docs/12.x/eloquent-resources">API Resources</a></li>
<li><a href="/docs/12.x/eloquent-serialization">Serialization</a></li>
<li><a href="/docs/12.x/eloquent-factories">Factories</a></li>
</ul>
</li>
<li>
<h2>AI</h2>
<ul>
<li><a href="/docs/12.x/ai-sdk">AI SDK</a></li>
<li><a href="/docs/12.x/mcp">MCP</a></li>
<li><a href="/docs/12.x/boost">Boost</a></li>
</ul>
</li>
<li>
<h2>Testing</h2>
<ul>
<li><a href="/docs/12.x/testing">Getting Started</a></li>
<li><a href="/docs/12.x/http-tests">HTTP Tests</a></li>
<li><a href="/docs/12.x/console-tests">Console Tests</a></li>
<li><a href="/docs/12.x/dusk">Browser Tests</a></li>
<li><a href="/docs/12.x/database-testing">Database</a></li>
<li><a href="/docs/12.x/mocking">Mocking</a></li>
</ul>
</li>
<li>
<h2>Packages</h2>
<ul>
<li><a href="/docs/12.x/billing">Cashier (Stripe)</a></li>
<li><a href="/docs/12.x/cashier-paddle">Cashier (Paddle)</a></li>
<li><a href="/docs/12.x/dusk">Dusk</a></li>
<li><a href="/docs/12.x/envoy">Envoy</a></li>
<li><a href="/docs/12.x/fortify">Fortify</a></li>
<li><a href="/docs/12.x/folio">Folio</a></li>
<li><a href="/docs/12.x/homestead">Homestead</a></li>
<li><a href="/docs/12.x/horizon">Horizon</a></li>
<li><a href="/docs/12.x/mix">Mix</a></li>
<li><a href="/docs/12.x/octane">Octane</a></li>
<li><a href="/docs/12.x/passport">Passport</a></li>
<li><a href="/docs/12.x/pennant">Pennant</a></li>
<li><a href="/docs/12.x/pint">Pint</a></li>
<li><a href="/docs/12.x/precognition">Precognition</a></li>
<li><a href="/docs/12.x/prompts">Prompts</a></li>
<li><a href="/docs/12.x/pulse">Pulse</a></li>
<li><a href="/docs/12.x/reverb">Reverb</a></li>
<li><a href="/docs/12.x/sail">Sail</a></li>
<li><a href="/docs/12.x/sanctum">Sanctum</a></li>
<li><a href="/docs/12.x/scout">Scout</a></li>
<li><a href="/docs/12.x/socialite">Socialite</a></li>
<li><a href="/docs/12.x/telescope">Telescope</a></li>
<li><a href="/docs/12.x/valet">Valet</a></li>
</ul>
</li>
<li><a href="https://api.laravel.com/docs/12.x">API Documentation</a></li>
<li><a href="/docs/changelog">Changelog</a></li></ul>

                                </div>
                            </nav>
                        </div>
                    </div>
                </aside>

                <section class="col-span-12 lg:col-span-9 xl:col-span-6">
                    <div>
                        <section>
                            <section class="docs_main max-w-prose">
                                
                                
                                <div id="main-content" class="contains-code-blocks">
    <h1>Eloquent: Getting Started</h1>
<ul>
<li><a href="#introduction">Introduction</a></li>
<li><a href="#generating-model-classes">Generating Model Classes</a></li>
<li><a href="#eloquent-model-conventions">Eloquent Model Conventions</a>
<ul>
<li><a href="#table-names">Table Names</a></li>
<li><a href="#primary-keys">Primary Keys</a></li>
<li><a href="#uuid-and-ulid-keys">UUID and ULID Keys</a></li>
<li><a href="#timestamps">Timestamps</a></li>
<li><a href="#database-connections">Database Connections</a></li>
<li><a href="#default-attribute-values">Default Attribute Values</a></li>
<li><a href="#configuring-eloquent-strictness">Configuring Eloquent Strictness</a></li>
</ul>
</li>
<li><a href="#retrieving-models">Retrieving Models</a>
<ul>
<li><a href="#collections">Collections</a></li>
<li><a href="#chunking-results">Chunking Results</a></li>
<li><a href="#chunking-using-lazy-collections">Chunk Using Lazy Collections</a></li>
<li><a href="#cursors">Cursors</a></li>
<li><a href="#advanced-subqueries">Advanced Subqueries</a></li>
</ul>
</li>
<li><a href="#retrieving-single-models">Retrieving Single Models / Aggregates</a>
<ul>
<li><a href="#retrieving-or-creating-models">Retrieving or Creating Models</a></li>
<li><a href="#retrieving-aggregates">Retrieving Aggregates</a></li>
</ul>
</li>
<li><a href="#inserting-and-updating-models">Inserting and Updating Models</a>
<ul>
<li><a href="#inserts">Inserts</a></li>
<li><a href="#updates">Updates</a></li>
<li><a href="#mass-assignment">Mass Assignment</a></li>
<li><a href="#upserts">Upserts</a></li>
</ul>
</li>
<li><a href="#deleting-models">Deleting Models</a>
<ul>
<li><a href="#soft-deleting">Soft Deleting</a></li>
<li><a href="#querying-soft-deleted-models">Querying Soft Deleted Models</a></li>
</ul>
</li>
<li><a href="#pruning-models">Pruning Models</a></li>
<li><a href="#replicating-models">Replicating Models</a></li>
<li><a href="#query-scopes">Query Scopes</a>
<ul>
<li><a href="#global-scopes">Global Scopes</a></li>
<li><a href="#local-scopes">Local Scopes</a></li>
<li><a href="#pending-attributes">Pending Attributes</a></li>
</ul>
</li>
<li><a href="#comparing-models">Comparing Models</a></li>
<li><a href="#events">Events</a>
<ul>
<li><a href="#events-using-closures">Using Closures</a></li>
<li><a href="#observers">Observers</a></li>
<li><a href="#muting-events">Muting Events</a></li>
</ul>
</li>
</ul>
<h2 id="introduction"><a href="#introduction">Introduction</a></h2>
<p>Laravel includes Eloquent, an object-relational mapper (ORM) that makes it enjoyable to interact with your database. When using Eloquent, each database table has a corresponding &quot;Model&quot; that is used to interact with that table. In addition to retrieving records from the database table, Eloquent models allow you to insert, update, and delete records from the table as well.</p>
<div class="flex flex-col p-3 mb-10 space-y-4 text-base leading-normal border rounded-md lg:px-4 lg:flex-row lg:space-y-0 lg:space-x-4 border-sand-light-5 callout dark:border-sand-dark-5 dark:text-sand-light-3 text-sand-dark-3">
    <div class="w-8 h-8 p-2 lg:my-1.5 rounded-xs flex items-center justify-center shrink-0 bg-[#8D54C5]">
        <svg width="16" height="21" viewBox="0 0 16 21" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M5 20H11M5.5 14H10.5M15 8C15 4.13401 11.866 1 8 1C4.13401 1 1 4.13401 1 8C1 10.7924 2.63505 13.2029 5 14.3264V17H11V14.3264C13.3649 13.2029 15 10.7924 15 8Z" stroke="#FDFDFC" stroke-width="1.5" stroke-linecap="square"/>
</svg>

    </div>
    <p class="callout text-pretty">
Before getting started, be sure to configure a database connection in your application's <code>config/database.php</code> configuration file. For more information on configuring your database, check out <a href="/docs/12.x/database#configuration">the database configuration documentation</a>.</p>
</div>
<h2 id="generating-model-classes"><a href="#generating-model-classes">Generating Model Classes</a></h2>
<p>To get started, let's create an Eloquent model. Models typically live in the <code>app\Models</code> directory and extend the <code>Illuminate\Database\Eloquent\Model</code> class. You may use the <code>make:model</code> <a href="/docs/12.x/artisan">Artisan command</a> to generate a new model:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="shell" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:model</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">Flight</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
php artisan make:model Flight</div></code></pre>
</div>
<p>If you would like to generate a <a href="/docs/12.x/migrations">database migration</a> when you generate the model, you may use the <code>--migration</code> or <code>-m</code> option:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="shell" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:model</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">--migration</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
php artisan make:model Flight --migration</div></code></pre>
</div>
<p>You may generate various other types of classes when generating a model, such as factories, seeders, policies, controllers, and form requests. In addition, these options may be combined to create multiple classes at once:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="shell" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #697098;">#</span><span style="color: #697098;"> Generate a model and a FlightFactory class...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:model</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">--factory</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:model</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">-f</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #697098;">#</span><span style="color: #697098;"> Generate a model and a FlightSeeder class...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:model</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">--seed</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:model</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">-s</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #697098;">#</span><span style="color: #697098;"> Generate a model and a FlightController class...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:model</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">--controller</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:model</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">-c</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #697098;">#</span><span style="color: #697098;"> Generate a model, FlightController resource class, and form request classes...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:model</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">--controller</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">--resource</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">--requests</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:model</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">-crR</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #697098;">#</span><span style="color: #697098;"> Generate a model and a FlightPolicy class...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:model</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">--policy</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">19</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">20</span><span style="color: #697098;">#</span><span style="color: #697098;"> Generate a model and a migration, factory, seeder, and controller...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">21</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:model</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">-mfsc</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">22</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">23</span><span style="color: #697098;">#</span><span style="color: #697098;"> Shortcut to generate a model, migration, factory, seeder, policy, controller, and form requests...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">24</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:model</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">--all</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">25</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:model</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">-a</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">26</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">27</span><span style="color: #697098;">#</span><span style="color: #697098;"> Generate a pivot model...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">28</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:model</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">Member</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">--pivot</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">29</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:model</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">Member</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">-p</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
# Generate a model and a FlightFactory class...
php artisan make:model Flight --factory
php artisan make:model Flight -f

# Generate a model and a FlightSeeder class

php artisan make:model Flight --seed
php artisan make:model Flight -s

# Generate a model and a FlightController class

php artisan make:model Flight --controller
php artisan make:model Flight -c

# Generate a model, FlightController resource class, and form request classes

php artisan make:model Flight --controller --resource --requests
php artisan make:model Flight -crR

# Generate a model and a FlightPolicy class

php artisan make:model Flight --policy

# Generate a model and a migration, factory, seeder, and controller

php artisan make:model Flight -mfsc

# Shortcut to generate a model, migration, factory, seeder, policy, controller, and form requests

php artisan make:model Flight --all
php artisan make:model Flight -a

# Generate a pivot model

php artisan make:model Member --pivot
php artisan make:model Member -p</div></code></pre>
</div>
<h4 id="inspecting-models"><a href="#inspecting-models">Inspecting Models</a></h4>
<p>Sometimes it can be difficult to determine all of a model's available attributes and relationships just by skimming its code. Instead, try the <code>model:show</code> Artisan command, which provides a convenient overview of all the model's attributes and relations:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="shell" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">model:show</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">Flight</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
php artisan model:show Flight</div></code></pre>
</div>
<h2 id="eloquent-model-conventions"><a href="#eloquent-model-conventions">Eloquent Model Conventions</a></h2>
<p>Models generated by the <code>make:model</code> command will be placed in the <code>app/Models</code> directory. Let's examine a basic model class and discuss some of Eloquent's key conventions:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    // ...
}</div></code></pre>
</div>
<h3 id="table-names"><a href="#table-names">Table Names</a></h3>
<p>After glancing at the example above, you may have noticed that we did not tell Eloquent which database table corresponds to our <code>Flight</code> model. By convention, the &quot;snake case&quot;, plural name of the class will be used as the table name unless another name is explicitly specified. So, in this case, Eloquent will assume the <code>Flight</code> model stores records in the <code>flights</code> table, while an <code>AirTrafficController</code> model would store records in an <code>air_traffic_controllers</code> table.</p>
<p>If your model's corresponding database table does not fit this convention, you may manually specify the model's table name by defining a <code>table</code> property on the model:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #697098;">     * The table associated with the model.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #697098;">     *</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #697098;">     * </span><span style="color: #C792EA;">@var</span><span style="color: #697098;"> </span><span style="color: #C792EA;">string</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$table</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">my_flights</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    /**
     *The table associated with the model.
     *
     *@var string
     */
    protected $table = &#39;my_flights&#39;;
}</div></code></pre>
</div>
<h3 id="primary-keys"><a href="#primary-keys">Primary Keys</a></h3>
<p>Eloquent will also assume that each model's corresponding database table has a primary key column named <code>id</code>. If necessary, you may define a protected <code>$primaryKey</code> property on your model to specify a different column that serves as your model's primary key:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #697098;">     * The primary key associated with the table.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #697098;">     *</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #697098;">     * </span><span style="color: #C792EA;">@var</span><span style="color: #697098;"> </span><span style="color: #C792EA;">string</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$primaryKey</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">flight_id</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    /**
     *The primary key associated with the table.
     *
     *@var string
     */
    protected $primaryKey = &#39;flight_id&#39;;
}</div></code></pre>
</div>
<p>In addition, Eloquent assumes that the primary key is an incrementing integer value, which means that Eloquent will automatically cast the primary key to an integer. If you wish to use a non-incrementing or a non-numeric primary key you must define a public <code>$incrementing</code> property on your model that is set to <code>false</code>:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #697098;">     * Indicates if the model&#39;s ID is auto-incrementing.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #697098;">     *</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #697098;">     * </span><span style="color: #C792EA;">@var</span><span style="color: #697098;"> </span><span style="color: #C792EA;">bool</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$incrementing</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">false</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

class Flight extends Model
{
    /**
     *Indicates if the model&#39;s ID is auto-incrementing.
     *
     *@var bool
     */
    public $incrementing = false;
}</div></code></pre>
</div>
<p>If your model's primary key is not an integer, you should define a protected <code>$keyType</code> property on your model. This property should have a value of <code>string</code>:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #697098;">     * The data type of the primary key ID.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #697098;">     *</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #697098;">     * </span><span style="color: #C792EA;">@var</span><span style="color: #697098;"> </span><span style="color: #C792EA;">string</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$keyType</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">string</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

class Flight extends Model
{
    /**
     *The data type of the primary key ID.
     *
     *@var string
     */
    protected $keyType = &#39;string&#39;;
}</div></code></pre>
</div>
<h4 id="composite-primary-keys"><a href="#composite-primary-keys">&quot;Composite&quot; Primary Keys</a></h4>
<p>Eloquent requires each model to have at least one uniquely identifying &quot;ID&quot; that can serve as its primary key. &quot;Composite&quot; primary keys are not supported by Eloquent models. However, you are free to add additional multi-column, unique indexes to your database tables in addition to the table's uniquely identifying primary key.</p>
<h3 id="uuid-and-ulid-keys"><a href="#uuid-and-ulid-keys">UUID and ULID Keys</a></h3>
<p>Instead of using auto-incrementing integers as your Eloquent model's primary keys, you may choose to use UUIDs instead. UUIDs are universally unique alpha-numeric identifiers that are 36 characters long.</p>
<p>If you would like a model to use a UUID key instead of an auto-incrementing integer key, you may use the <code>Illuminate\Database\Eloquent\Concerns\HasUuids</code> trait on the model. Of course, you should ensure that the model has a <a href="/docs/12.x/migrations#column-method-uuid">UUID equivalent primary key column</a>:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\Concerns\</span><span style="color: #FFCB8B;">HasUuids</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">Article</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">HasUuids</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">}</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BEC5D4;">$article</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Article</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">create</span><span style="color: #BFC7D5;">([</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">title</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Traveling to Europe</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">]);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #BEC5D4;">$article</span><span style="color: #89DDFF;">-&gt;id</span><span style="color: #BFC7D5;">; </span><span style="color: #697098;">//</span><span style="color: #697098;"> &quot;8f8e8478-9035-4d23-b9a7-62f4d2612ce5&quot;</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use Illuminate\Database\Eloquent\Concerns\HasUuids;
use Illuminate\Database\Eloquent\Model;

class Article extends Model
{
    use HasUuids;

    // ...
}

$article = Article::create([&#39;title&#39; =&gt; &#39;Traveling to Europe&#39;]);

$article-&gt;id; // &quot;8f8e8478-9035-4d23-b9a7-62f4d2612ce5&quot;</div></code></pre>
</div>
<p>By default, The <code>HasUuids</code> trait will generate <a href="/docs/12.x/strings#method-str-ordered-uuid">&quot;ordered&quot; UUIDs</a> for your models. These UUIDs are more efficient for indexed database storage because they can be sorted lexicographically.</p>
<p>You can override the UUID generation process for a given model by defining a <code>newUniqueId</code> method on the model. In addition, you may specify which columns should receive UUIDs by defining a <code>uniqueIds</code> method on the model:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Ramsey\Uuid\</span><span style="color: #FFCB8B;">Uuid</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span><span style="color: #697098;"> * Generate a new UUID for the model.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #697098;"> </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">newUniqueId</span><span style="color: #D9F5DD;">()</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">string</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">return</span><span style="color: #BFC7D5;"> (</span><span style="color: #C792EA;">string</span><span style="color: #BFC7D5;">) </span><span style="color: #FFCB8B;">Uuid</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">uuid4</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">}</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #697098;"> * Get the columns that should receive a unique identifier.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #697098;"> *</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #697098;"> * </span><span style="color: #C792EA;">@return</span><span style="color: #697098;"> </span><span style="color: #C792EA;">array</span><span style="color: #697098;">&lt;</span><span style="color: #C792EA;">int</span><span style="color: #697098;">, string&gt;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #697098;"> </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">uniqueIds</span><span style="color: #D9F5DD;">()</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">array</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">return</span><span style="color: #BFC7D5;"> [</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">id</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">discount_code</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">];</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">19</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use Ramsey\Uuid\Uuid;

/**

* Generate a new UUID for the model.
 */
public function newUniqueId(): string
{
    return (string) Uuid::uuid4();
}

/**

* Get the columns that should receive a unique identifier.
*
* @return array&lt;int, string&gt;
 */
public function uniqueIds(): array
{
    return [&#39;id&#39;, &#39;discount_code&#39;];
}</div></code></pre>

</div>
<p>If you wish, you may choose to utilize &quot;ULIDs&quot; instead of UUIDs. ULIDs are similar to UUIDs; however, they are only 26 characters in length. Like ordered UUIDs, ULIDs are lexicographically sortable for efficient database indexing. To utilize ULIDs, you should use the <code>Illuminate\Database\Eloquent\Concerns\HasUlids</code> trait on your model. You should also ensure that the model has a <a href="/docs/12.x/migrations#column-method-ulid">ULID equivalent primary key column</a>:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\Concerns\</span><span style="color: #FFCB8B;">HasUlids</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">Article</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">HasUlids</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">}</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BEC5D4;">$article</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Article</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">create</span><span style="color: #BFC7D5;">([</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">title</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Traveling to Asia</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">]);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #BEC5D4;">$article</span><span style="color: #89DDFF;">-&gt;id</span><span style="color: #BFC7D5;">; </span><span style="color: #697098;">//</span><span style="color: #697098;"> &quot;01gd4d3tgrrfqeda94gdbtdk5c&quot;</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use Illuminate\Database\Eloquent\Concerns\HasUlids;
use Illuminate\Database\Eloquent\Model;

class Article extends Model
{
    use HasUlids;

    // ...
}

$article = Article::create([&#39;title&#39; =&gt; &#39;Traveling to Asia&#39;]);

$article-&gt;id; // &quot;01gd4d3tgrrfqeda94gdbtdk5c&quot;</div></code></pre>
</div>
<h3 id="timestamps"><a href="#timestamps">Timestamps</a></h3>
<p>By default, Eloquent expects <code>created_at</code> and <code>updated_at</code> columns to exist on your model's corresponding database table. Eloquent will automatically set these column's values when models are created or updated. If you do not want these columns to be automatically managed by Eloquent, you should define a <code>$timestamps</code> property on your model with a value of <code>false</code>:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #697098;">     * Indicates if the model should be timestamped.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #697098;">     *</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #697098;">     * </span><span style="color: #C792EA;">@var</span><span style="color: #697098;"> </span><span style="color: #C792EA;">bool</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$timestamps</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">false</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    /**
     *Indicates if the model should be timestamped.
     *
     *@var bool
     */
    public $timestamps = false;
}</div></code></pre>
</div>
<p>If you need to customize the format of your model's timestamps, set the <code>$dateFormat</code> property on your model. This property determines how date attributes are stored in the database as well as their format when the model is serialized to an array or JSON:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #697098;">     * The storage format of the model&#39;s date columns.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #697098;">     *</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #697098;">     * </span><span style="color: #C792EA;">@var</span><span style="color: #697098;"> </span><span style="color: #C792EA;">string</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$dateFormat</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">U</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    /**
     *The storage format of the model&#39;s date columns.
     *
     *@var string
     */
    protected $dateFormat = &#39;U&#39;;
}</div></code></pre>
</div>
<p>If you need to customize the names of the columns used to store the timestamps, you may define <code>CREATED_AT</code> and <code>UPDATED_AT</code> constants on your model:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #697098;">     * The name of the &quot;created at&quot; column.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #697098;">     *</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #697098;">     * </span><span style="color: #C792EA;">@var</span><span style="color: #697098;"> </span><span style="color: #C792EA;">string</span><span style="color: #697098;">|</span><span style="color: #C792EA;">null</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">const</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">CREATED_AT</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">creation_date</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #697098;">     * The name of the &quot;updated at&quot; column.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #697098;">     *</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #697098;">     * </span><span style="color: #C792EA;">@var</span><span style="color: #697098;"> </span><span style="color: #C792EA;">string</span><span style="color: #697098;">|</span><span style="color: #C792EA;">null</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">const</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">UPDATED_AT</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">updated_date</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

class Flight extends Model
{
    /**
     *The name of the &quot;created at&quot; column.
     *
     *@var string|null
     */
    public const CREATED_AT = &#39;creation_date&#39;;

    /**
     * The name of the &quot;updated at&quot; column.
     *
     * @var string|null
     */
    public const UPDATED_AT = &#39;updated_date&#39;;
}</div></code></pre>
</div>
<p>If you would like to perform model operations without the model having its <code>updated_at</code> timestamp modified, you may operate on the model within a closure given to the <code>withoutTimestamps</code> method:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #FFCB8B;">Model</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">withoutTimestamps</span><span style="color: #BFC7D5;">(</span><span style="color: #C792EA;">fn</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">()</span><span style="color: #BFC7D5;"> =&gt; </span><span style="color: #BEC5D4;">$post</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">increment</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">reads</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">));</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
Model::withoutTimestamps(fn () =&gt; $post-&gt;increment(&#39;reads&#39;));</div></code></pre>
</div>
<h3 id="database-connections"><a href="#database-connections">Database Connections</a></h3>
<p>By default, all Eloquent models will use the default database connection that is configured for your application. If you would like to specify a different connection that should be used when interacting with a particular model, you should define a <code>$connection</code> property on the model:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #697098;">     * The database connection that should be used by the model.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #697098;">     *</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #697098;">     * </span><span style="color: #C792EA;">@var</span><span style="color: #697098;"> </span><span style="color: #C792EA;">string</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$connection</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">mysql</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    /**
     *The database connection that should be used by the model.
     *
     *@var string
     */
    protected $connection = &#39;mysql&#39;;
}</div></code></pre>
</div>
<h3 id="default-attribute-values"><a href="#default-attribute-values">Default Attribute Values</a></h3>
<p>By default, a newly instantiated model instance will not contain any attribute values. If you would like to define the default values for some of your model's attributes, you may define an <code>$attributes</code> property on your model. Attribute values placed in the <code>$attributes</code> array should be in their raw, &quot;storable&quot; format as if they were just read from the database:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #697098;">     * The model&#39;s default values for attributes.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #697098;">     *</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #697098;">     * </span><span style="color: #C792EA;">@var</span><span style="color: #697098;"> </span><span style="color: #C792EA;">array</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$attributes</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> [</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">        </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">options</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">[]</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #BFC7D5;">        </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">delayed</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">false</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #BFC7D5;">    ];</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    /**
     *The model&#39;s default values for attributes.
     *
     *@var array
     */
    protected $attributes = [
        &#39;options&#39; =&gt; &#39;[]&#39;,
        &#39;delayed&#39; =&gt; false,
    ];
}</div></code></pre>
</div>
<h3 id="configuring-eloquent-strictness"><a href="#configuring-eloquent-strictness">Configuring Eloquent Strictness</a></h3>
<p>Laravel offers several methods that allow you to configure Eloquent's behavior and &quot;strictness&quot; in a variety of situations.</p>
<p>First, the <code>preventLazyLoading</code> method accepts an optional boolean argument that indicates if lazy loading should be prevented. For example, you may wish to only disable lazy loading in non-production environments so that your production environment will continue to function normally even if a lazy loaded relationship is accidentally present in production code. Typically, this method should be invoked in the <code>boot</code> method of your application's <code>AppServiceProvider</code>:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #697098;"> * Bootstrap any application services.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #697098;"> </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">boot</span><span style="color: #D9F5DD;">()</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">7</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">8</span><span style="color: #BFC7D5;">    </span><span style="color: #FFCB8B;">Model</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">preventLazyLoading</span><span style="color: #BFC7D5;">(</span><span style="color: #C792EA;">!</span><span style="color: #BFC7D5;"> </span><span style="color: #FF5572;">$this</span><span style="color: #89DDFF;">-&gt;app-&gt;</span><span style="color: #82AAFF;">isProduction</span><span style="color: #BFC7D5;">());</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">9</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use Illuminate\Database\Eloquent\Model;

/**

* Bootstrap any application services.
 */
public function boot(): void
{
    Model::preventLazyLoading(! $this-&gt;app-&gt;isProduction());
}</div></code></pre>

</div>
<p>Also, you may instruct Laravel to throw an exception when attempting to fill an unfillable attribute by invoking the <code>preventSilentlyDiscardingAttributes</code> method. This can help prevent unexpected errors during local development when attempting to set an attribute that has not been added to the model's <code>fillable</code> array:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #FFCB8B;">Model</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">preventSilentlyDiscardingAttributes</span><span style="color: #BFC7D5;">(</span><span style="color: #C792EA;">!</span><span style="color: #BFC7D5;"> </span><span style="color: #FF5572;">$this</span><span style="color: #89DDFF;">-&gt;app-&gt;</span><span style="color: #82AAFF;">isProduction</span><span style="color: #BFC7D5;">());</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
Model::preventSilentlyDiscardingAttributes(! $this-&gt;app-&gt;isProduction());</div></code></pre>
</div>
<h2 id="retrieving-models"><a href="#retrieving-models">Retrieving Models</a></h2>
<p>Once you have created a model and <a href="/docs/12.x/migrations#generating-migrations">its associated database table</a>, you are ready to start retrieving data from your database. You can think of each Eloquent model as a powerful <a href="/docs/12.x/queries">query builder</a> allowing you to fluently query the database table associated with the model. The model's <code>all</code> method will retrieve all of the records from the model's associated database table:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">Flight</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #C792EA;">foreach</span><span style="color: #BFC7D5;"> (</span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">all</span><span style="color: #BFC7D5;">() </span><span style="color: #C792EA;">as</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;">) {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">echo</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;name</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\Flight;

foreach (Flight::all() as $flight) {
    echo $flight-&gt;name;
}</div></code></pre>
</div>
<h4 id="building-queries"><a href="#building-queries">Building Queries</a></h4>
<p>The Eloquent <code>all</code> method will return all of the results in the model's table. However, since each Eloquent model serves as a <a href="/docs/12.x/queries">query builder</a>, you may add additional constraints to queries and then invoke the <code>get</code> method to retrieve the results:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$flights</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">active</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">orderBy</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">limit</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">10</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">get</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$flights = Flight::where(&#39;active&#39;, 1)
    -&gt;orderBy(&#39;name&#39;)
    -&gt;limit(10)
    -&gt;get();</div></code></pre>
</div>
<div class="flex flex-col p-3 mb-10 space-y-4 text-base leading-normal border rounded-md lg:px-4 lg:flex-row lg:space-y-0 lg:space-x-4 border-sand-light-5 callout dark:border-sand-dark-5 dark:text-sand-light-3 text-sand-dark-3">
    <div class="w-8 h-8 p-2 lg:my-1.5 rounded-xs flex items-center justify-center shrink-0 bg-[#8D54C5]">
        <svg width="16" height="21" viewBox="0 0 16 21" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M5 20H11M5.5 14H10.5M15 8C15 4.13401 11.866 1 8 1C4.13401 1 1 4.13401 1 8C1 10.7924 2.63505 13.2029 5 14.3264V17H11V14.3264C13.3649 13.2029 15 10.7924 15 8Z" stroke="#FDFDFC" stroke-width="1.5" stroke-linecap="square"/>
</svg>

    </div>
    <p class="callout text-pretty">
Since Eloquent models are query builders, you should review all of the methods provided by Laravel's <a href="/docs/12.x/queries">query builder</a>. You may use any of these methods when writing your Eloquent queries.</p>
</div>
<h4 id="refreshing-models"><a href="#refreshing-models">Refreshing Models</a></h4>
<p>If you already have an instance of an Eloquent model that was retrieved from the database, you can &quot;refresh&quot; the model using the <code>fresh</code> and <code>refresh</code> methods. The <code>fresh</code> method will re-retrieve the model from the database. The existing model instance will not be affected:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">number</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">FR 900</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">first</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BEC5D4;">$freshFlight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">fresh</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$flight = Flight::where(&#39;number&#39;, &#39;FR 900&#39;)-&gt;first();

$freshFlight = $flight-&gt;fresh();</div></code></pre>
</div>
<p>The <code>refresh</code> method will re-hydrate the existing model using fresh data from the database. In addition, all of its loaded relationships will be refreshed as well:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">number</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">FR 900</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">first</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;number</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">FR 456</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">refresh</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">7</span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;number</span><span style="color: #BFC7D5;">; </span><span style="color: #697098;">//</span><span style="color: #697098;"> &quot;FR 900&quot;</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$flight = Flight::where(&#39;number&#39;, &#39;FR 900&#39;)-&gt;first();

$flight-&gt;number = &#39;FR 456&#39;;

$flight-&gt;refresh();

$flight-&gt;number; // &quot;FR 900&quot;</div></code></pre>
</div>
<h3 id="collections"><a href="#collections">Collections</a></h3>
<p>As we have seen, Eloquent methods like <code>all</code> and <code>get</code> retrieve multiple records from the database. However, these methods don't return a plain PHP array. Instead, an instance of <code>Illuminate\Database\Eloquent\Collection</code> is returned.</p>
<p>The Eloquent <code>Collection</code> class extends Laravel's base <code>Illuminate\Support\Collection</code> class, which provides a <a href="/docs/12.x/collections#available-methods">variety of helpful methods</a> for interacting with data collections. For example, the <code>reject</code> method may be used to remove models from a collection based on the results of an invoked closure:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$flights</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">destination</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Paris</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">get</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BEC5D4;">$flights</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$flights</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">reject</span><span style="color: #BFC7D5;">(</span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$flight</span><span style="color: #D9F5DD;">)</span><span style="color: #BFC7D5;"> {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">return</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;cancelled</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BFC7D5;">});</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$flights = Flight::where(&#39;destination&#39;, &#39;Paris&#39;)-&gt;get();

$flights = $flights-&gt;reject(function (Flight $flight) {
    return $flight-&gt;cancelled;
});</div></code></pre>
</div>
<p>In addition to the methods provided by Laravel's base collection class, the Eloquent collection class provides <a href="/docs/12.x/eloquent-collections#available-methods">a few extra methods</a> that are specifically intended for interacting with collections of Eloquent models.</p>
<p>Since all of Laravel's collections implement PHP's iterable interfaces, you may loop over collections as if they were an array:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">foreach</span><span style="color: #BFC7D5;"> (</span><span style="color: #BEC5D4;">$flights</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">as</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;">) {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">echo</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;name</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
foreach ($flights as $flight) {
    echo $flight-&gt;name;
}</div></code></pre>
</div>
<h3 id="chunking-results"><a href="#chunking-results">Chunking Results</a></h3>
<p>Your application may run out of memory if you attempt to load tens of thousands of Eloquent records via the <code>all</code> or <code>get</code> methods. Instead of using these methods, the <code>chunk</code> method may be used to process large numbers of models more efficiently.</p>
<p>The <code>chunk</code> method will retrieve a subset of Eloquent models, passing them to a closure for processing. Since only the current chunk of Eloquent models is retrieved at a time, the <code>chunk</code> method will provide significantly reduced memory usage when working with a large number of models:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">Flight</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Collection</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">chunk</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">200</span><span style="color: #BFC7D5;">, </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">Collection</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$flights</span><span style="color: #D9F5DD;">)</span><span style="color: #BFC7D5;"> {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">foreach</span><span style="color: #BFC7D5;"> (</span><span style="color: #BEC5D4;">$flights</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">as</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;">) {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span><span style="color: #BFC7D5;">        </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">7</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">8</span><span style="color: #BFC7D5;">});</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\Flight;
use Illuminate\Database\Eloquent\Collection;

Flight::chunk(200, function (Collection $flights) {
    foreach ($flights as $flight) {
        // ...
    }
});</div></code></pre>
</div>
<p>The first argument passed to the <code>chunk</code> method is the number of records you wish to receive per &quot;chunk&quot;. The closure passed as the second argument will be invoked for each chunk that is retrieved from the database. A database query will be executed to retrieve each chunk of records passed to the closure.</p>
<p>If you are filtering the results of the <code>chunk</code> method based on a column that you will also be updating while iterating over the results, you should use the <code>chunkById</code> method. Using the <code>chunk</code> method in these scenarios could lead to unexpected and inconsistent results. Internally, the <code>chunkById</code> method will always retrieve models with an <code>id</code> column greater than the last model in the previous chunk:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">departed</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #82AAFF;">true</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">chunkById</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">200</span><span style="color: #BFC7D5;">, </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">Collection</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$flights</span><span style="color: #D9F5DD;">)</span><span style="color: #BFC7D5;"> {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">        </span><span style="color: #BEC5D4;">$flights</span><span style="color: #89DDFF;">-&gt;each-&gt;</span><span style="color: #82AAFF;">update</span><span style="color: #BFC7D5;">([</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">departed</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">false</span><span style="color: #BFC7D5;">]);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">    }, column: </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">id</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">);</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
Flight::where(&#39;departed&#39;, true)
    -&gt;chunkById(200, function (Collection $flights) {
        $flights-&gt;each-&gt;update([&#39;departed&#39; =&gt; false]);
    }, column: &#39;id&#39;);</div></code></pre>
</div>
<p>Since the <code>chunkById</code> and <code>lazyById</code> methods add their own &quot;where&quot; conditions to the query being executed, you should typically <a href="/docs/12.x/queries#logical-grouping">logically group</a> your own conditions within a closure:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">(</span><span style="color: #BEC5D4;">$query</span><span style="color: #D9F5DD;">)</span><span style="color: #BFC7D5;"> {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #BEC5D4;">$query</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">delayed</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #82AAFF;">true</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">orWhere</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">cancelled</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #82AAFF;">true</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">})</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">chunkById</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">200</span><span style="color: #BFC7D5;">, </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">Collection</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$flights</span><span style="color: #D9F5DD;">)</span><span style="color: #BFC7D5;"> {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">    </span><span style="color: #BEC5D4;">$flights</span><span style="color: #89DDFF;">-&gt;each-&gt;</span><span style="color: #82AAFF;">update</span><span style="color: #BFC7D5;">([</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BFC7D5;">        </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">departed</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">false</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span><span style="color: #BFC7D5;">        </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">cancelled</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">true</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">7</span><span style="color: #BFC7D5;">    ]);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">8</span><span style="color: #BFC7D5;">}, column: </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">id</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">);</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
Flight::where(function ($query) {
    $query-&gt;where(&#39;delayed&#39;, true)-&gt;orWhere(&#39;cancelled&#39;, true);
})-&gt;chunkById(200, function (Collection $flights) {
    $flights-&gt;each-&gt;update([
        &#39;departed&#39; =&gt; false,
        &#39;cancelled&#39; =&gt; true
    ]);
}, column: &#39;id&#39;);</div></code></pre>
</div>
<h3 id="chunking-using-lazy-collections"><a href="#chunking-using-lazy-collections">Chunking Using Lazy Collections</a></h3>
<p>The <code>lazy</code> method works similarly to <a href="#chunking-results">the <code>chunk</code> method</a> in the sense that, behind the scenes, it executes the query in chunks. However, instead of passing each chunk directly into a callback as is, the <code>lazy</code> method returns a flattened <a href="/docs/12.x/collections#lazy-collections">LazyCollection</a> of Eloquent models, which lets you interact with the results as a single stream:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">Flight</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #C792EA;">foreach</span><span style="color: #BFC7D5;"> (</span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">lazy</span><span style="color: #BFC7D5;">() </span><span style="color: #C792EA;">as</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;">) {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\Flight;

foreach (Flight::lazy() as $flight) {
    // ...
}</div></code></pre>
</div>
<p>If you are filtering the results of the <code>lazy</code> method based on a column that you will also be updating while iterating over the results, you should use the <code>lazyById</code> method. Internally, the <code>lazyById</code> method will always retrieve models with an <code>id</code> column greater than the last model in the previous chunk:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">departed</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #82AAFF;">true</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">lazyById</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">200</span><span style="color: #BFC7D5;">, column: </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">id</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">-&gt;each-&gt;</span><span style="color: #82AAFF;">update</span><span style="color: #BFC7D5;">([</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">departed</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">false</span><span style="color: #BFC7D5;">]);</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
Flight::where(&#39;departed&#39;, true)
    -&gt;lazyById(200, column: &#39;id&#39;)
    -&gt;each-&gt;update([&#39;departed&#39; =&gt; false]);</div></code></pre>
</div>
<p>You may filter the results based on the descending order of the <code>id</code> using the <code>lazyByIdDesc</code> method.</p>
<h3 id="cursors"><a href="#cursors">Cursors</a></h3>
<p>Similar to the <code>lazy</code> method, the <code>cursor</code> method may be used to significantly reduce your application's memory consumption when iterating through tens of thousands of Eloquent model records.</p>
<p>The <code>cursor</code> method will only execute a single database query; however, the individual Eloquent models will not be hydrated until they are actually iterated over. Therefore, only one Eloquent model is kept in memory at any given time while iterating over the cursor.</p>
<div class="flex flex-col p-3 mb-10 space-y-4 text-base leading-normal border rounded-md lg:px-4 lg:flex-row lg:space-y-0 lg:space-x-4 border-sand-light-5 callout dark:border-sand-dark-5 dark:text-sand-light-3 text-sand-dark-3">
    <div class="w-8 h-8 p-2 lg:my-1.5 rounded-xs flex items-center justify-center shrink-0 bg-[#F53003]">
        <svg width="2" height="18" viewBox="0 0 2 18" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M1 17V16.99M1 1V13" stroke="#FDFDFC" stroke-width="2" stroke-linecap="square"/>
</svg>

    </div>
    <p class="callout text-pretty">
Since the <code>cursor</code> method only ever holds a single Eloquent model in memory at a time, it cannot eager load relationships. If you need to eager load relationships, consider using <a href="#chunking-using-lazy-collections">the <code>lazy</code> method</a> instead.</p>
</div>
<p>Internally, the <code>cursor</code> method uses PHP <a href="https://www.php.net/manual/en/language.generators.overview.php">generators</a> to implement this functionality:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">Flight</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #C792EA;">foreach</span><span style="color: #BFC7D5;"> (</span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">destination</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Zurich</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">cursor</span><span style="color: #BFC7D5;">() </span><span style="color: #C792EA;">as</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;">) {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\Flight;

foreach (Flight::where(&#39;destination&#39;, &#39;Zurich&#39;)-&gt;cursor() as $flight) {
    // ...
}</div></code></pre>
</div>
<p>The <code>cursor</code> returns an <code>Illuminate\Support\LazyCollection</code> instance. <a href="/docs/12.x/collections#lazy-collections">Lazy collections</a> allow you to use many of the collection methods available on typical Laravel collections while only loading a single model into memory at a time:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">User</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BEC5D4;">$users</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">cursor</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">filter</span><span style="color: #BFC7D5;">(</span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">User</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$user</span><span style="color: #D9F5DD;">)</span><span style="color: #BFC7D5;"> {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">return</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;id</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #F78C6C;">500</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BFC7D5;">});</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">7</span><span style="color: #C792EA;">foreach</span><span style="color: #BFC7D5;"> (</span><span style="color: #BEC5D4;">$users</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">as</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$user</span><span style="color: #BFC7D5;">) {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">8</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">echo</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;id</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">9</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\User;

$users = User::cursor()-&gt;filter(function (User $user) {
    return $user-&gt;id &gt; 500;
});

foreach ($users as $user) {
    echo $user-&gt;id;
}</div></code></pre>
</div>
<p>Although the <code>cursor</code> method uses far less memory than a regular query (by only holding a single Eloquent model in memory at a time), it will still eventually run out of memory. This is <a href="https://www.php.net/manual/en/mysqlinfo.concepts.buffering.php">due to PHP's PDO driver internally caching all raw query results in its buffer</a>. If you're dealing with a very large number of Eloquent records, consider using <a href="#chunking-using-lazy-collections">the <code>lazy</code> method</a> instead.</p>
<h3 id="advanced-subqueries"><a href="#advanced-subqueries">Advanced Subqueries</a></h3>
<h4 id="subquery-selects"><a href="#subquery-selects">Subquery Selects</a></h4>
<p>Eloquent also offers advanced subquery support, which allows you to pull information from related tables in a single query. For example, let's imagine that we have a table of flight <code>destinations</code> and a table of <code>flights</code> to destinations. The <code>flights</code> table contains an <code>arrived_at</code> column which indicates when the flight arrived at the destination.</p>
<p>Using the subquery functionality available to the query builder's <code>select</code> and <code>addSelect</code> methods, we can select all of the <code>destinations</code> and the name of the flight that most recently arrived at that destination using a single query:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">Destination</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">Flight</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #C792EA;">return</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Destination</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">addSelect</span><span style="color: #BFC7D5;">([</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">last_flight</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">select</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">whereColumn</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">destination_id</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">destinations.id</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">orderByDesc</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">arrived_at</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">7</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">limit</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">8</span><span style="color: #BFC7D5;">])</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">get</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\Destination;
use App\Models\Flight;

return Destination::addSelect([&#39;last_flight&#39; =&gt; Flight::select(&#39;name&#39;)
    -&gt;whereColumn(&#39;destination_id&#39;, &#39;destinations.id&#39;)
    -&gt;orderByDesc(&#39;arrived_at&#39;)
    -&gt;limit(1)
])-&gt;get();</div></code></pre>
</div>
<h4 id="subquery-ordering"><a href="#subquery-ordering">Subquery Ordering</a></h4>
<p>In addition, the query builder's <code>orderBy</code> function supports subqueries. Continuing to use our flight example, we may use this functionality to sort all destinations based on when the last flight arrived at that destination. Again, this may be done while executing a single database query:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">return</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Destination</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">orderByDesc</span><span style="color: #BFC7D5;">(</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">select</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">arrived_at</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">        </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">whereColumn</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">destination_id</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">destinations.id</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">        </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">orderByDesc</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">arrived_at</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BFC7D5;">        </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">limit</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">get</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
return Destination::orderByDesc(
    Flight::select(&#39;arrived_at&#39;)
        -&gt;whereColumn(&#39;destination_id&#39;, &#39;destinations.id&#39;)
        -&gt;orderByDesc(&#39;arrived_at&#39;)
        -&gt;limit(1)
)-&gt;get();</div></code></pre>
</div>
<h2 id="retrieving-single-models"><a href="#retrieving-single-models">Retrieving Single Models / Aggregates</a></h2>
<p>In addition to retrieving all of the records matching a given query, you may also retrieve single records using the <code>find</code>, <code>first</code>, or <code>firstWhere</code> methods. Instead of returning a collection of models, these methods return a single model instance:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">Flight</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #697098;">//</span><span style="color: #697098;"> Retrieve a model by its primary key...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">find</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #697098;">//</span><span style="color: #697098;"> Retrieve the first model matching the query constraints...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">active</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">first</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #697098;">//</span><span style="color: #697098;"> Alternative to retrieving the first model matching the query constraints...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">firstWhere</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">active</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">);</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\Flight;

// Retrieve a model by its primary key...
$flight = Flight::find(1);

// Retrieve the first model matching the query constraints...
$flight = Flight::where(&#39;active&#39;, 1)-&gt;first();

// Alternative to retrieving the first model matching the query constraints...
$flight = Flight::firstWhere(&#39;active&#39;, 1);</div></code></pre>
</div>
<p>Sometimes you may wish to perform some other action if no results are found. The <code>findOr</code> and <code>firstOr</code> methods will return a single model instance or, if no results are found, execute the given closure. The value returned by the closure will be considered the result of the method:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">findOr</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">, </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">()</span><span style="color: #BFC7D5;"> {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">});</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">legs</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">&gt;</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">3</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">firstOr</span><span style="color: #BFC7D5;">(</span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">()</span><span style="color: #BFC7D5;"> {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">7</span><span style="color: #BFC7D5;">});</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$flight = Flight::findOr(1, function () {
    // ...
});

$flight = Flight::where(&#39;legs&#39;, &#39;&gt;&#39;, 3)-&gt;firstOr(function () {
    // ...
});</div></code></pre>
</div>
<h4 id="not-found-exceptions"><a href="#not-found-exceptions">Not Found Exceptions</a></h4>
<p>Sometimes you may wish to throw an exception if a model is not found. This is particularly useful in routes or controllers. The <code>findOrFail</code> and <code>firstOrFail</code> methods will retrieve the first result of the query; however, if no result is found, an <code>Illuminate\Database\Eloquent\ModelNotFoundException</code> will be thrown:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">findOrFail</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">legs</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">&gt;</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">3</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">firstOrFail</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$flight = Flight::findOrFail(1);

$flight = Flight::where(&#39;legs&#39;, &#39;&gt;&#39;, 3)-&gt;firstOrFail();</div></code></pre>
</div>
<p>If the <code>ModelNotFoundException</code> is not caught, a 404 HTTP response is automatically sent back to the client:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">Flight</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #FFCB8B;">Route</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">get</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">/api/flights/{id}</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">(</span><span style="color: #C792EA;">string</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$id</span><span style="color: #D9F5DD;">)</span><span style="color: #BFC7D5;"> {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">return</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">findOrFail</span><span style="color: #BFC7D5;">(</span><span style="color: #BEC5D4;">$id</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BFC7D5;">});</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\Flight;

Route::get(&#39;/api/flights/{id}&#39;, function (string $id) {
    return Flight::findOrFail($id);
});</div></code></pre>
</div>
<h3 id="retrieving-or-creating-models"><a href="#retrieving-or-creating-models">Retrieving or Creating Models</a></h3>
<p>The <code>firstOrCreate</code> method will attempt to locate a database record using the given column / value pairs. If the model cannot be found in the database, a record will be inserted with the attributes resulting from merging the first array argument with the optional second array argument.</p>
<p>The <code>firstOrNew</code> method, like <code>firstOrCreate</code>, will attempt to locate a record in the database matching the given attributes. However, if a model is not found, a new model instance will be returned. Note that the model returned by <code>firstOrNew</code> has not yet been persisted to the database. You will need to manually call the <code>save</code> method to persist it:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">Flight</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #697098;">//</span><span style="color: #697098;"> Retrieve flight by name or create it if it doesn&#39;t exist...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">firstOrCreate</span><span style="color: #BFC7D5;">([</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">London to Paris</span><span style="color: #D9F5DD;">&#39;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #BFC7D5;">]);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #697098;">//</span><span style="color: #697098;"> Retrieve flight by name or create it with the name, delayed, and arrival_time attributes...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">firstOrCreate</span><span style="color: #BFC7D5;">(</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">    [</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">London to Paris</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">],</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BFC7D5;">    [</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">delayed</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">arrival_time</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">11:30</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">]</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #697098;">//</span><span style="color: #697098;"> Retrieve flight by name or instantiate a new Flight instance...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">firstOrNew</span><span style="color: #BFC7D5;">([</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">London to Paris</span><span style="color: #D9F5DD;">&#39;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #BFC7D5;">]);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">19</span><span style="color: #697098;">//</span><span style="color: #697098;"> Retrieve flight by name or instantiate with the name, delayed, and arrival_time attributes...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">20</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">firstOrNew</span><span style="color: #BFC7D5;">(</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">21</span><span style="color: #BFC7D5;">    [</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Tokyo to Sydney</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">],</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">22</span><span style="color: #BFC7D5;">    [</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">delayed</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">arrival_time</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">11:30</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">]</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">23</span><span style="color: #BFC7D5;">);</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\Flight;

// Retrieve flight by name or create it if it doesn&#39;t exist...
$flight = Flight::firstOrCreate([
    &#39;name&#39; =&gt; &#39;London to Paris&#39;
]);

// Retrieve flight by name or create it with the name, delayed, and arrival_time attributes...
$flight = Flight::firstOrCreate(
    [&#39;name&#39; =&gt; &#39;London to Paris&#39;],
    [&#39;delayed&#39; =&gt; 1, &#39;arrival_time&#39; =&gt; &#39;11:30&#39;]
);

// Retrieve flight by name or instantiate a new Flight instance...
$flight = Flight::firstOrNew([
    &#39;name&#39; =&gt; &#39;London to Paris&#39;
]);

// Retrieve flight by name or instantiate with the name, delayed, and arrival_time attributes...
$flight = Flight::firstOrNew(
    [&#39;name&#39; =&gt; &#39;Tokyo to Sydney&#39;],
    [&#39;delayed&#39; =&gt; 1, &#39;arrival_time&#39; =&gt; &#39;11:30&#39;]
);</div></code></pre>
</div>
<h3 id="retrieving-aggregates"><a href="#retrieving-aggregates">Retrieving Aggregates</a></h3>
<p>When interacting with Eloquent models, you may also use the <code>count</code>, <code>sum</code>, <code>max</code>, and other <a href="/docs/12.x/queries#aggregates">aggregate methods</a> provided by the Laravel <a href="/docs/12.x/queries">query builder</a>. As you might expect, these methods return a scalar value instead of an Eloquent model instance:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$count</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">active</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">count</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BEC5D4;">$max</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">active</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">max</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">price</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">);</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$count = Flight::where(&#39;active&#39;, 1)-&gt;count();

$max = Flight::where(&#39;active&#39;, 1)-&gt;max(&#39;price&#39;);</div></code></pre>
</div>
<h2 id="inserting-and-updating-models"><a href="#inserting-and-updating-models">Inserting and Updating Models</a></h2>
<h3 id="inserts"><a href="#inserts">Inserts</a></h3>
<p>Of course, when using Eloquent, we don't only need to retrieve models from the database. We also need to insert new records. Thankfully, Eloquent makes it simple. To insert a new record into the database, you should instantiate a new model instance and set attributes on the model. Then, call the <code>save</code> method on the model instance:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Http\Controllers;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">Flight</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Http\</span><span style="color: #FFCB8B;">RedirectResponse</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Http\</span><span style="color: #FFCB8B;">Request</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">FlightController</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Controller</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #697098;">     * Store a new flight in the database.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">store</span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">Request</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$request</span><span style="color: #D9F5DD;">)</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">RedirectResponse</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">    {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #BFC7D5;">        </span><span style="color: #697098;">//</span><span style="color: #697098;"> Validate the request...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span><span style="color: #BFC7D5;">        </span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">new</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">19</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">20</span><span style="color: #BFC7D5;">        </span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;name</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$request</span><span style="color: #89DDFF;">-&gt;name</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">21</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">22</span><span style="color: #BFC7D5;">        </span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">save</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">23</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">24</span><span style="color: #BFC7D5;">        </span><span style="color: #C792EA;">return</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">redirect</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">/flights</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">25</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">26</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Http\Controllers;

use App\Models\Flight;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;

class FlightController extends Controller
{
    /**
     *Store a new flight in the database.
     */
    public function store(Request $request): RedirectResponse
    {
        // Validate the request...

        $flight = new Flight;

        $flight-&gt;name = $request-&gt;name;

        $flight-&gt;save();

        return redirect(&#39;/flights&#39;);
    }
}</div></code></pre>
</div>
<p>In this example, we assign the <code>name</code> field from the incoming HTTP request to the <code>name</code> attribute of the <code>App\Models\Flight</code> model instance. When we call the <code>save</code> method, a record will be inserted into the database. The model's <code>created_at</code> and <code>updated_at</code> timestamps will automatically be set when the <code>save</code> method is called, so there is no need to set them manually.</p>
<p>Alternatively, you may use the <code>create</code> method to &quot;save&quot; a new model using a single PHP statement. The inserted model instance will be returned to you by the <code>create</code> method:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">Flight</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">create</span><span style="color: #BFC7D5;">([</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">London to Paris</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BFC7D5;">]);</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\Flight;

$flight = Flight::create([
    &#39;name&#39; =&gt; &#39;London to Paris&#39;,
]);</div></code></pre>
</div>
<p>However, before using the <code>create</code> method, you will need to specify either a <code>fillable</code> or <code>guarded</code> property on your model class. These properties are required because all Eloquent models are protected against mass assignment vulnerabilities by default. To learn more about mass assignment, please consult the <a href="#mass-assignment">mass assignment documentation</a>.</p>
<h3 id="updates"><a href="#updates">Updates</a></h3>
<p>The <code>save</code> method may also be used to update models that already exist in the database. To update a model, you should retrieve it and set any attributes you wish to update. Then, you should call the model's <code>save</code> method. Again, the <code>updated_at</code> timestamp will automatically be updated, so there is no need to manually set its value:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">Flight</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">find</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;name</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Paris to London</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">7</span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">save</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\Flight;

$flight = Flight::find(1);

$flight-&gt;name = &#39;Paris to London&#39;;

$flight-&gt;save();</div></code></pre>
</div>
<p>Occasionally, you may need to update an existing model or create a new model if no matching model exists. Like the <code>firstOrCreate</code> method, the <code>updateOrCreate</code> method persists the model, so there's no need to manually call the <code>save</code> method.</p>
<p>In the example below, if a flight exists with a <code>departure</code> location of <code>Oakland</code> and a <code>destination</code> location of <code>San Diego</code>, its <code>price</code> and <code>discounted</code> columns will be updated. If no such flight exists, a new flight will be created which has the attributes resulting from merging the first argument array with the second argument array:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">updateOrCreate</span><span style="color: #BFC7D5;">(</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    [</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">departure</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Oakland</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">destination</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">San Diego</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">],</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">    [</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">price</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #F78C6C;">99</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">discounted</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">]</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">);</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$flight = Flight::updateOrCreate(
    [&#39;departure&#39; =&gt; &#39;Oakland&#39;, &#39;destination&#39; =&gt; &#39;San Diego&#39;],
    [&#39;price&#39; =&gt; 99, &#39;discounted&#39; =&gt; 1]
);</div></code></pre>
</div>
<p>When using methods such as <code>firstOrCreate</code> or <code>updateOrCreate</code>, you may not know whether a new model has been created or an existing one has been updated. The <code>wasRecentlyCreated</code> property indicates if the model was created during its current lifecycle:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">updateOrCreate</span><span style="color: #BFC7D5;">(</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #C792EA;">if</span><span style="color: #BFC7D5;"> (</span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;wasRecentlyCreated</span><span style="color: #BFC7D5;">) {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">//</span><span style="color: #697098;"> New flight record was inserted...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">7</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$flight = Flight::updateOrCreate(
    // ...
);

if ($flight-&gt;wasRecentlyCreated) {
    // New flight record was inserted...
}</div></code></pre>
</div>
<h4 id="mass-updates"><a href="#mass-updates">Mass Updates</a></h4>
<p>Updates can also be performed against models that match a given query. In this example, all flights that are <code>active</code> and have a <code>destination</code> of <code>San Diego</code> will be marked as delayed:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">active</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">destination</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">San Diego</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">update</span><span style="color: #BFC7D5;">([</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">delayed</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">]);</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
Flight::where(&#39;active&#39;, 1)
    -&gt;where(&#39;destination&#39;, &#39;San Diego&#39;)
    -&gt;update([&#39;delayed&#39; =&gt; 1]);</div></code></pre>
</div>
<p>The <code>update</code> method expects an array of column and value pairs representing the columns that should be updated. The <code>update</code> method returns the number of affected rows.</p>
<div class="flex flex-col p-3 mb-10 space-y-4 text-base leading-normal border rounded-md lg:px-4 lg:flex-row lg:space-y-0 lg:space-x-4 border-sand-light-5 callout dark:border-sand-dark-5 dark:text-sand-light-3 text-sand-dark-3">
    <div class="w-8 h-8 p-2 lg:my-1.5 rounded-xs flex items-center justify-center shrink-0 bg-[#F53003]">
        <svg width="2" height="18" viewBox="0 0 2 18" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M1 17V16.99M1 1V13" stroke="#FDFDFC" stroke-width="2" stroke-linecap="square"/>
</svg>

    </div>
    <p class="callout text-pretty">
When issuing a mass update via Eloquent, the <code>saving</code>, <code>saved</code>, <code>updating</code>, and <code>updated</code> model events will not be fired for the updated models. This is because the models are never actually retrieved when issuing a mass update.</p>
</div>
<h4 id="examining-attribute-changes"><a href="#examining-attribute-changes">Examining Attribute Changes</a></h4>
<p>Eloquent provides the <code>isDirty</code>, <code>isClean</code>, and <code>wasChanged</code> methods to examine the internal state of your model and determine how its attributes have changed from when the model was originally retrieved.</p>
<p>The <code>isDirty</code> method determines if any of the model's attributes have been changed since the model was retrieved. You may pass a specific attribute name or an array of attributes to the <code>isDirty</code> method to determine if any of the attributes are &quot;dirty&quot;. The <code>isClean</code> method will determine if an attribute has remained unchanged since the model was retrieved. This method also accepts an optional attribute argument:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">User</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #BEC5D4;">$user</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">create</span><span style="color: #BFC7D5;">([</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">first_name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Taylor</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">last_name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Otwell</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">title</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Developer</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #BFC7D5;">]);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;title</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Painter</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">isDirty</span><span style="color: #BFC7D5;">(); </span><span style="color: #697098;">//</span><span style="color: #697098;"> true</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">isDirty</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">title</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">); </span><span style="color: #697098;">//</span><span style="color: #697098;"> true</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">isDirty</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">first_name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">); </span><span style="color: #697098;">//</span><span style="color: #697098;"> false</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">isDirty</span><span style="color: #BFC7D5;">([</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">first_name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">title</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">]); </span><span style="color: #697098;">//</span><span style="color: #697098;"> true</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">isClean</span><span style="color: #BFC7D5;">(); </span><span style="color: #697098;">//</span><span style="color: #697098;"> false</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">isClean</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">title</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">); </span><span style="color: #697098;">//</span><span style="color: #697098;"> false</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">isClean</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">first_name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">); </span><span style="color: #697098;">//</span><span style="color: #697098;"> true</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">19</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">isClean</span><span style="color: #BFC7D5;">([</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">first_name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">title</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">]); </span><span style="color: #697098;">//</span><span style="color: #697098;"> false</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">20</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">21</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">save</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">22</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">23</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">isDirty</span><span style="color: #BFC7D5;">(); </span><span style="color: #697098;">//</span><span style="color: #697098;"> false</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">24</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">isClean</span><span style="color: #BFC7D5;">(); </span><span style="color: #697098;">//</span><span style="color: #697098;"> true</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\User;

$user = User::create([
    &#39;first_name&#39; =&gt; &#39;Taylor&#39;,
    &#39;last_name&#39; =&gt; &#39;Otwell&#39;,
    &#39;title&#39; =&gt; &#39;Developer&#39;,
]);

$user-&gt;title = &#39;Painter&#39;;

$user-&gt;isDirty(); // true
$user-&gt;isDirty(&#39;title&#39;); // true
$user-&gt;isDirty(&#39;first_name&#39;); // false
$user-&gt;isDirty([&#39;first_name&#39;, &#39;title&#39;]); // true

$user-&gt;isClean(); // false
$user-&gt;isClean(&#39;title&#39;); // false
$user-&gt;isClean(&#39;first_name&#39;); // true
$user-&gt;isClean([&#39;first_name&#39;, &#39;title&#39;]); // false

$user-&gt;save();

$user-&gt;isDirty(); // false
$user-&gt;isClean(); // true</div></code></pre>
</div>
<p>The <code>wasChanged</code> method determines if any attributes were changed when the model was last saved within the current request cycle. If needed, you may pass an attribute name to see if a particular attribute was changed:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #BEC5D4;">$user</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">create</span><span style="color: #BFC7D5;">([</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">first_name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Taylor</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">last_name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Otwell</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">title</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Developer</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #BFC7D5;">]);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;title</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Painter</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">save</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">wasChanged</span><span style="color: #BFC7D5;">(); </span><span style="color: #697098;">//</span><span style="color: #697098;"> true</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">wasChanged</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">title</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">); </span><span style="color: #697098;">//</span><span style="color: #697098;"> true</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">wasChanged</span><span style="color: #BFC7D5;">([</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">title</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">slug</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">]); </span><span style="color: #697098;">//</span><span style="color: #697098;"> true</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">wasChanged</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">first_name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">); </span><span style="color: #697098;">//</span><span style="color: #697098;"> false</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">wasChanged</span><span style="color: #BFC7D5;">([</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">first_name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">title</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">]); </span><span style="color: #697098;">//</span><span style="color: #697098;"> true</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$user = User::create([
    &#39;first_name&#39; =&gt; &#39;Taylor&#39;,
    &#39;last_name&#39; =&gt; &#39;Otwell&#39;,
    &#39;title&#39; =&gt; &#39;Developer&#39;,
]);

$user-&gt;title = &#39;Painter&#39;;

$user-&gt;save();

$user-&gt;wasChanged(); // true
$user-&gt;wasChanged(&#39;title&#39;); // true
$user-&gt;wasChanged([&#39;title&#39;, &#39;slug&#39;]); // true
$user-&gt;wasChanged(&#39;first_name&#39;); // false
$user-&gt;wasChanged([&#39;first_name&#39;, &#39;title&#39;]); // true</div></code></pre>
</div>
<p>The <code>getOriginal</code> method returns an array containing the original attributes of the model regardless of any changes to the model since it was retrieved. If needed, you may pass a specific attribute name to get the original value of a particular attribute:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #BEC5D4;">$user</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">find</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;name</span><span style="color: #BFC7D5;">; </span><span style="color: #697098;">//</span><span style="color: #697098;"> John</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;email</span><span style="color: #BFC7D5;">; </span><span style="color: #697098;">//</span><span style="color: #697098;"> <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="acc6c3c4c2ecc9d4cdc1dcc0c982cfc3c1">[email&#160;protected]</a></span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;name</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Jack</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;name</span><span style="color: #BFC7D5;">; </span><span style="color: #697098;">//</span><span style="color: #697098;"> Jack</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">getOriginal</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">); </span><span style="color: #697098;">//</span><span style="color: #697098;"> John</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">getOriginal</span><span style="color: #BFC7D5;">(); </span><span style="color: #697098;">//</span><span style="color: #697098;"> Array of original attributes...</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$user = User::find(1);

$user-&gt;name; // John
$user-&gt;email; // <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="fb91949395bb9e839a968b979ed5989496">[email&#160;protected]</a>

$user-&gt;name = &#39;Jack&#39;;
$user-&gt;name; // Jack

$user-&gt;getOriginal(&#39;name&#39;); // John
$user-&gt;getOriginal(); // Array of original attributes...</div></code></pre>
</div>
<p>The <code>getChanges</code> method returns an array containing the attributes that changed when the model was last saved, while the <code>getPrevious</code> method returns an array containing the original attribute values before the model was last saved:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #BEC5D4;">$user</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">find</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;name</span><span style="color: #BFC7D5;">; </span><span style="color: #697098;">//</span><span style="color: #697098;"> John</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;email</span><span style="color: #BFC7D5;">; </span><span style="color: #697098;">//</span><span style="color: #697098;"> <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="5e343136301e3b263f332e323b703d3133">[email&#160;protected]</a></span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">update</span><span style="color: #BFC7D5;">([</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Jack</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">email</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;"><a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="6d070c0e062d08150c001d0108430e0200">[email&#160;protected]</a></span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">]);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">getChanges</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #697098;">/*</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #697098;">    [</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #697098;">        &#39;name&#39; =&gt; &#39;Jack&#39;,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #697098;">        &#39;email&#39; =&gt; &#39;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="94fef5f7ffd4f1ecf5f9e4f8f1baf7fbf9">[email&#160;protected]</a>&#39;,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #697098;">    ]</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">19</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">20</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">getPrevious</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">21</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">22</span><span style="color: #697098;">/*</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">23</span><span style="color: #697098;">    [</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">24</span><span style="color: #697098;">        &#39;name&#39; =&gt; &#39;John&#39;,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">25</span><span style="color: #697098;">        &#39;email&#39; =&gt; &#39;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="8be1e4e3e5cbeef3eae6fbe7eea5e8e4e6">[email&#160;protected]</a>&#39;,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">26</span><span style="color: #697098;">    ]</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">27</span><span style="color: #697098;">*/</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$user = User::find(1);

$user-&gt;name; // John
$user-&gt;email; // <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="caa0a5a2a48aafb2aba7baa6afe4a9a5a7">[email&#160;protected]</a>

$user-&gt;update([
    &#39;name&#39; =&gt; &#39;Jack&#39;,
    &#39;email&#39; =&gt; &#39;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="f892999b93b89d80999588949dd69b9795">[email&#160;protected]</a>&#39;,
]);

$user-&gt;getChanges();

/*
    [
        &#39;name&#39; =&gt; &#39;Jack&#39;,
        &#39;email&#39; =&gt; &#39;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="97fdf6f4fcd7f2eff6fae7fbf2b9f4f8fa">[email&#160;protected]</a>&#39;,
    ]
*/

$user-&gt;getPrevious();

/*
    [
        &#39;name&#39; =&gt; &#39;John&#39;,
        &#39;email&#39; =&gt; &#39;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="7812171016381d00191508141d561b1715">[email&#160;protected]</a>&#39;,
    ]
*/</div></code></pre>
</div>
<h3 id="mass-assignment"><a href="#mass-assignment">Mass Assignment</a></h3>
<p>You may use the <code>create</code> method to &quot;save&quot; a new model using a single PHP statement. The inserted model instance will be returned to you by the method:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">Flight</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">create</span><span style="color: #BFC7D5;">([</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">London to Paris</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BFC7D5;">]);</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\Flight;

$flight = Flight::create([
    &#39;name&#39; =&gt; &#39;London to Paris&#39;,
]);</div></code></pre>
</div>
<p>However, before using the <code>create</code> method, you will need to specify either a <code>fillable</code> or <code>guarded</code> property on your model class. These properties are required because all Eloquent models are protected against mass assignment vulnerabilities by default.</p>
<p>A mass assignment vulnerability occurs when a user passes an unexpected HTTP request field and that field changes a column in your database that you did not expect. For example, a malicious user might send an <code>is_admin</code> parameter through an HTTP request, which is then passed to your model's <code>create</code> method, allowing the user to escalate themselves to an administrator.</p>
<p>So, to get started, you should define which model attributes you want to make mass assignable. You may do this using the <code>$fillable</code> property on the model. For example, let's make the <code>name</code> attribute of our <code>Flight</code> model mass assignable:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #697098;">     * The attributes that are mass assignable.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #697098;">     *</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #697098;">     * </span><span style="color: #C792EA;">@var</span><span style="color: #697098;"> </span><span style="color: #C792EA;">array</span><span style="color: #697098;">&lt;</span><span style="color: #C792EA;">int</span><span style="color: #697098;">, string&gt;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$fillable</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> [</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">];</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    /**
     *The attributes that are mass assignable.
     *
     *@var array&lt;int, string&gt;
     */
    protected $fillable = [&#39;name&#39;];
}</div></code></pre>
</div>
<p>Once you have specified which attributes are mass assignable, you may use the <code>create</code> method to insert a new record in the database. The <code>create</code> method returns the newly created model instance:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">create</span><span style="color: #BFC7D5;">([</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">London to Paris</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">]);</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$flight = Flight::create([&#39;name&#39; =&gt; &#39;London to Paris&#39;]);</div></code></pre>
</div>
<p>If you already have a model instance, you may use the <code>fill</code> method to populate it with an array of attributes:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">fill</span><span style="color: #BFC7D5;">([</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">name</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Amsterdam to Frankfurt</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">]);</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$flight-&gt;fill([&#39;name&#39; =&gt; &#39;Amsterdam to Frankfurt&#39;]);</div></code></pre>
</div>
<h4 id="mass-assignment-json-columns"><a href="#mass-assignment-json-columns">Mass Assignment and JSON Columns</a></h4>
<p>When assigning JSON columns, each column's mass assignable key must be specified in your model's <code>$fillable</code> array. For security, Laravel does not support updating nested JSON attributes when using the <code>guarded</code> property:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #697098;"> * The attributes that are mass assignable.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #697098;"> *</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #697098;"> * </span><span style="color: #C792EA;">@var</span><span style="color: #697098;"> </span><span style="color: #C792EA;">array</span><span style="color: #697098;">&lt;</span><span style="color: #C792EA;">int</span><span style="color: #697098;">, string&gt;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #697098;"> </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$fillable</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> [</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">7</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">options-&gt;enabled</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">8</span><span style="color: #BFC7D5;">];</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
/**
 * The attributes that are mass assignable.
 *
 * @var array&lt;int, string&gt;
 */
protected $fillable = [
    &#39;options-&gt;enabled&#39;,
];</div></code></pre>
</div>
<h4 id="allowing-mass-assignment"><a href="#allowing-mass-assignment">Allowing Mass Assignment</a></h4>
<p>If you would like to make all of your attributes mass assignable, you may define your model's <code>$guarded</code> property as an empty array. If you choose to unguard your model, you should take special care to always hand-craft the arrays passed to Eloquent's <code>fill</code>, <code>create</code>, and <code>update</code> methods:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #697098;"> * The attributes that aren&#39;t mass assignable.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #697098;"> *</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #697098;"> * </span><span style="color: #C792EA;">@var</span><span style="color: #697098;"> </span><span style="color: #C792EA;">array</span><span style="color: #697098;">&lt;</span><span style="color: #C792EA;">string</span><span style="color: #697098;">&gt;|</span><span style="color: #C792EA;">bool</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #697098;"> </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$guarded</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> [];</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
/**
 * The attributes that aren&#39;t mass assignable.
 *
 * @var array&lt;string&gt;|bool
 */
protected $guarded = [];</div></code></pre>
</div>
<h4 id="mass-assignment-exceptions"><a href="#mass-assignment-exceptions">Mass Assignment Exceptions</a></h4>
<p>By default, attributes that are not included in the <code>$fillable</code> array are silently discarded when performing mass-assignment operations. In production, this is expected behavior; however, during local development it can lead to confusion as to why model changes are not taking effect.</p>
<p>If you wish, you may instruct Laravel to throw an exception when attempting to fill an unfillable attribute by invoking the <code>preventSilentlyDiscardingAttributes</code> method. Typically, this method should be invoked in the <code>boot</code> method of your application's <code>AppServiceProvider</code> class:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #697098;"> * Bootstrap any application services.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #697098;"> </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">boot</span><span style="color: #D9F5DD;">()</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">7</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">8</span><span style="color: #BFC7D5;">    </span><span style="color: #FFCB8B;">Model</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">preventSilentlyDiscardingAttributes</span><span style="color: #BFC7D5;">(</span><span style="color: #FF5572;">$this</span><span style="color: #89DDFF;">-&gt;app-&gt;</span><span style="color: #82AAFF;">isLocal</span><span style="color: #BFC7D5;">());</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">9</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use Illuminate\Database\Eloquent\Model;

/**

* Bootstrap any application services.
 */
public function boot(): void
{
    Model::preventSilentlyDiscardingAttributes($this-&gt;app-&gt;isLocal());
}</div></code></pre>

</div>
<h3 id="upserts"><a href="#upserts">Upserts</a></h3>
<p>Eloquent's <code>upsert</code> method may be used to update or create records in a single, atomic operation. The method's first argument consists of the values to insert or update, while the second argument lists the column(s) that uniquely identify records within the associated table. The method's third and final argument is an array of the columns that should be updated if a matching record already exists in the database. The <code>upsert</code> method will automatically set the <code>created_at</code> and <code>updated_at</code> timestamps if timestamps are enabled on the model:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">upsert</span><span style="color: #BFC7D5;">([</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    [</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">departure</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Oakland</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">destination</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">San Diego</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">price</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #F78C6C;">99</span><span style="color: #BFC7D5;">],</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">    [</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">departure</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Chicago</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">destination</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">New York</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">price</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #F78C6C;">150</span><span style="color: #BFC7D5;">]</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">], uniqueBy: [</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">departure</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">destination</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">], update: [</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">price</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">]);</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
Flight::upsert([
    [&#39;departure&#39; =&gt; &#39;Oakland&#39;, &#39;destination&#39; =&gt; &#39;San Diego&#39;, &#39;price&#39; =&gt; 99],
    [&#39;departure&#39; =&gt; &#39;Chicago&#39;, &#39;destination&#39; =&gt; &#39;New York&#39;, &#39;price&#39; =&gt; 150]
], uniqueBy: [&#39;departure&#39;, &#39;destination&#39;], update: [&#39;price&#39;]);</div></code></pre>
</div>
<div class="flex flex-col p-3 mb-10 space-y-4 text-base leading-normal border rounded-md lg:px-4 lg:flex-row lg:space-y-0 lg:space-x-4 border-sand-light-5 callout dark:border-sand-dark-5 dark:text-sand-light-3 text-sand-dark-3">
    <div class="w-8 h-8 p-2 lg:my-1.5 rounded-xs flex items-center justify-center shrink-0 bg-[#F53003]">
        <svg width="2" height="18" viewBox="0 0 2 18" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M1 17V16.99M1 1V13" stroke="#FDFDFC" stroke-width="2" stroke-linecap="square"/>
</svg>

    </div>
    <p class="callout text-pretty">
All databases except SQL Server require the columns in the second argument of the <code>upsert</code> method to have a &quot;primary&quot; or &quot;unique&quot; index. In addition, the MariaDB and MySQL database drivers ignore the second argument of the <code>upsert</code> method and always use the &quot;primary&quot; and &quot;unique&quot; indexes of the table to detect existing records.</p>
</div>
<h2 id="deleting-models"><a href="#deleting-models">Deleting Models</a></h2>
<p>To delete a model, you may call the <code>delete</code> method on the model instance:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">Flight</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">find</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">delete</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\Flight;

$flight = Flight::find(1);

$flight-&gt;delete();</div></code></pre>
</div>
<h4 id="deleting-an-existing-model-by-its-primary-key"><a href="#deleting-an-existing-model-by-its-primary-key">Deleting an Existing Model by its Primary Key</a></h4>
<p>In the example above, we are retrieving the model from the database before calling the <code>delete</code> method. However, if you know the primary key of the model, you may delete the model without explicitly retrieving it by calling the <code>destroy</code> method. In addition to accepting the single primary key, the <code>destroy</code> method will accept multiple primary keys, an array of primary keys, or a <a href="/docs/12.x/collections">collection</a> of primary keys:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">destroy</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">destroy</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">2</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">3</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">destroy</span><span style="color: #BFC7D5;">([</span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">2</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">3</span><span style="color: #BFC7D5;">]);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">7</span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">destroy</span><span style="color: #BFC7D5;">(</span><span style="color: #82AAFF;">collect</span><span style="color: #BFC7D5;">([</span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">,</span><span style="color: #82AAFF;"> </span><span style="color: #F78C6C;">2</span><span style="color: #BFC7D5;">,</span><span style="color: #82AAFF;"> </span><span style="color: #F78C6C;">3</span><span style="color: #BFC7D5;">]));</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
Flight::destroy(1);

Flight::destroy(1, 2, 3);

Flight::destroy([1, 2, 3]);

Flight::destroy(collect([1, 2, 3]));</div></code></pre>
</div>
<p>If you are utilizing <a href="#soft-deleting">soft deleting models</a>, you may permanently delete models via the <code>forceDestroy</code> method:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">forceDestroy</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">);</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
Flight::forceDestroy(1);</div></code></pre>
</div>
<div class="flex flex-col p-3 mb-10 space-y-4 text-base leading-normal border rounded-md lg:px-4 lg:flex-row lg:space-y-0 lg:space-x-4 border-sand-light-5 callout dark:border-sand-dark-5 dark:text-sand-light-3 text-sand-dark-3">
    <div class="w-8 h-8 p-2 lg:my-1.5 rounded-xs flex items-center justify-center shrink-0 bg-[#F53003]">
        <svg width="2" height="18" viewBox="0 0 2 18" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M1 17V16.99M1 1V13" stroke="#FDFDFC" stroke-width="2" stroke-linecap="square"/>
</svg>

    </div>
    <p class="callout text-pretty">
The <code>destroy</code> method loads each model individually and calls the <code>delete</code> method so that the <code>deleting</code> and <code>deleted</code> events are properly dispatched for each model.</p>
</div>
<h4 id="deleting-models-using-queries"><a href="#deleting-models-using-queries">Deleting Models Using Queries</a></h4>
<p>Of course, you may build an Eloquent query to delete all models matching your query's criteria. In this example, we will delete all flights that are marked as inactive. Like mass updates, mass deletes will not dispatch model events for the models that are deleted:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$deleted</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">active</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">0</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">delete</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$deleted = Flight::where(&#39;active&#39;, 0)-&gt;delete();</div></code></pre>
</div>
<p>To delete all models in a table, you should execute a query without adding any conditions:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$deleted</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">query</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">delete</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$deleted = Flight::query()-&gt;delete();</div></code></pre>
</div>
<div class="flex flex-col p-3 mb-10 space-y-4 text-base leading-normal border rounded-md lg:px-4 lg:flex-row lg:space-y-0 lg:space-x-4 border-sand-light-5 callout dark:border-sand-dark-5 dark:text-sand-light-3 text-sand-dark-3">
    <div class="w-8 h-8 p-2 lg:my-1.5 rounded-xs flex items-center justify-center shrink-0 bg-[#F53003]">
        <svg width="2" height="18" viewBox="0 0 2 18" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M1 17V16.99M1 1V13" stroke="#FDFDFC" stroke-width="2" stroke-linecap="square"/>
</svg>

    </div>
    <p class="callout text-pretty">
When executing a mass delete statement via Eloquent, the <code>deleting</code> and <code>deleted</code> model events will not be dispatched for the deleted models. This is because the models are never actually retrieved when executing the delete statement.</p>
</div>
<h3 id="soft-deleting"><a href="#soft-deleting">Soft Deleting</a></h3>
<p>In addition to actually removing records from your database, Eloquent can also &quot;soft delete&quot; models. When models are soft deleted, they are not actually removed from your database. Instead, a <code>deleted_at</code> attribute is set on the model indicating the date and time at which the model was &quot;deleted&quot;. To enable soft deletes for a model, add the <code>Illuminate\Database\Eloquent\SoftDeletes</code> trait to the model:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">SoftDeletes</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">SoftDeletes</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class Flight extends Model
{
    use SoftDeletes;
}</div></code></pre>
</div>
<div class="flex flex-col p-3 mb-10 space-y-4 text-base leading-normal border rounded-md lg:px-4 lg:flex-row lg:space-y-0 lg:space-x-4 border-sand-light-5 callout dark:border-sand-dark-5 dark:text-sand-light-3 text-sand-dark-3">
    <div class="w-8 h-8 p-2 lg:my-1.5 rounded-xs flex items-center justify-center shrink-0 bg-[#8D54C5]">
        <svg width="16" height="21" viewBox="0 0 16 21" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M5 20H11M5.5 14H10.5M15 8C15 4.13401 11.866 1 8 1C4.13401 1 1 4.13401 1 8C1 10.7924 2.63505 13.2029 5 14.3264V17H11V14.3264C13.3649 13.2029 15 10.7924 15 8Z" stroke="#FDFDFC" stroke-width="1.5" stroke-linecap="square"/>
</svg>

    </div>
    <p class="callout text-pretty">
The <code>SoftDeletes</code> trait will automatically cast the <code>deleted_at</code> attribute to a <code>DateTime</code> / <code>Carbon</code> instance for you.</p>
</div>
<p>You should also add the <code>deleted_at</code> column to your database table. The Laravel <a href="/docs/12.x/migrations">schema builder</a> contains a helper method to create this column:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Schema\</span><span style="color: #FFCB8B;">Blueprint</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Support\Facades\</span><span style="color: #FFCB8B;">Schema</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span><span style="color: #FFCB8B;">Schema</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">table</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">flights</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">Blueprint</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$table</span><span style="color: #D9F5DD;">)</span><span style="color: #BFC7D5;"> {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #BFC7D5;">    </span><span style="color: #BEC5D4;">$table</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">softDeletes</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #BFC7D5;">});</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #FFCB8B;">Schema</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">table</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">flights</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">Blueprint</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$table</span><span style="color: #D9F5DD;">)</span><span style="color: #BFC7D5;"> {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">    </span><span style="color: #BEC5D4;">$table</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">dropSoftDeletes</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">});</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

Schema::table(&#39;flights&#39;, function (Blueprint $table) {
    $table-&gt;softDeletes();
});

Schema::table(&#39;flights&#39;, function (Blueprint $table) {
    $table-&gt;dropSoftDeletes();
});</div></code></pre>
</div>
<p>Now, when you call the <code>delete</code> method on the model, the <code>deleted_at</code> column will be set to the current date and time. However, the model's database record will be left in the table. When querying a model that uses soft deletes, the soft deleted models will automatically be excluded from all query results.</p>
<p>To determine if a given model instance has been soft deleted, you may use the <code>trashed</code> method:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">if</span><span style="color: #BFC7D5;"> (</span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">trashed</span><span style="color: #BFC7D5;">()) {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
if ($flight-&gt;trashed()) {
    // ...
}</div></code></pre>
</div>
<h4 id="restoring-soft-deleted-models"><a href="#restoring-soft-deleted-models">Restoring Soft Deleted Models</a></h4>
<p>Sometimes you may wish to &quot;un-delete&quot; a soft deleted model. To restore a soft deleted model, you may call the <code>restore</code> method on a model instance. The <code>restore</code> method will set the model's <code>deleted_at</code> column to <code>null</code>:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">restore</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$flight-&gt;restore();</div></code></pre>
</div>
<p>You may also use the <code>restore</code> method in a query to restore multiple models. Again, like other &quot;mass&quot; operations, this will not dispatch any model events for the models that are restored:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">withTrashed</span><span style="color: #BFC7D5;">()</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">airline_id</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">restore</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
Flight::withTrashed()
    -&gt;where(&#39;airline_id&#39;, 1)
    -&gt;restore();</div></code></pre>
</div>
<p>The <code>restore</code> method may also be used when building <a href="/docs/12.x/eloquent-relationships">relationship</a> queries:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">history</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">restore</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$flight-&gt;history()-&gt;restore();</div></code></pre>
</div>
<h4 id="permanently-deleting-models"><a href="#permanently-deleting-models">Permanently Deleting Models</a></h4>
<p>Sometimes you may need to truly remove a model from your database. You may use the <code>forceDelete</code> method to permanently remove a soft deleted model from the database table:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">forceDelete</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$flight-&gt;forceDelete();</div></code></pre>
</div>
<p>You may also use the <code>forceDelete</code> method when building Eloquent relationship queries:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">history</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">forceDelete</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$flight-&gt;history()-&gt;forceDelete();</div></code></pre>
</div>
<h3 id="querying-soft-deleted-models"><a href="#querying-soft-deleted-models">Querying Soft Deleted Models</a></h3>
<h4 id="including-soft-deleted-models"><a href="#including-soft-deleted-models">Including Soft Deleted Models</a></h4>
<p>As noted above, soft deleted models will automatically be excluded from query results. However, you may force soft deleted models to be included in a query's results by calling the <code>withTrashed</code> method on the query:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">Flight</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BEC5D4;">$flights</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">withTrashed</span><span style="color: #BFC7D5;">()</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">account_id</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">get</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\Flight;

$flights = Flight::withTrashed()
    -&gt;where(&#39;account_id&#39;, 1)
    -&gt;get();</div></code></pre>
</div>
<p>The <code>withTrashed</code> method may also be called when building a <a href="/docs/12.x/eloquent-relationships">relationship</a> query:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">history</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">withTrashed</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">get</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$flight-&gt;history()-&gt;withTrashed()-&gt;get();</div></code></pre>
</div>
<h4 id="retrieving-only-soft-deleted-models"><a href="#retrieving-only-soft-deleted-models">Retrieving Only Soft Deleted Models</a></h4>
<p>The <code>onlyTrashed</code> method will retrieve <strong>only</strong> soft deleted models:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$flights</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">onlyTrashed</span><span style="color: #BFC7D5;">()</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">airline_id</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">)</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">    </span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">get</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$flights = Flight::onlyTrashed()
    -&gt;where(&#39;airline_id&#39;, 1)
    -&gt;get();</div></code></pre>
</div>
<h2 id="pruning-models"><a href="#pruning-models">Pruning Models</a></h2>
<p>Sometimes you may want to periodically delete models that are no longer needed. To accomplish this, you may add the <code>Illuminate\Database\Eloquent\Prunable</code> or <code>Illuminate\Database\Eloquent\MassPrunable</code> trait to the models you would like to periodically prune. After adding one of the traits to the model, implement a <code>prunable</code> method which returns an Eloquent query builder that resolves the models that are no longer needed:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Builder</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Prunable</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Prunable</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #697098;">     * Get the prunable model query.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">prunable</span><span style="color: #D9F5DD;">()</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Builder</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #BFC7D5;">    {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span><span style="color: #BFC7D5;">        </span><span style="color: #C792EA;">return</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">static</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">created_at</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">&lt;=</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #82AAFF;">now</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">minus</span><span style="color: #BFC7D5;">(months: </span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">));</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">19</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">20</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Prunable;

class Flight extends Model
{
    use Prunable;

    /**
     * Get the prunable model query.
     */
    public function prunable(): Builder
    {
        return static::where(&#39;created_at&#39;, &#39;&lt;=&#39;, now()-&gt;minus(months: 1));
    }
}</div></code></pre>
</div>
<p>When marking models as <code>Prunable</code>, you may also define a <code>pruning</code> method on the model. This method will be called before the model is deleted. This method can be useful for deleting any additional resources associated with the model, such as stored files, before the model is permanently removed from the database:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #697098;"> * Prepare the model for pruning.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #697098;"> </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">pruning</span><span style="color: #D9F5DD;">()</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">7</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
/**
 * Prepare the model for pruning.
 */
protected function pruning(): void
{
    // ...
}</div></code></pre>
</div>
<p>After configuring your prunable model, you should schedule the <code>model:prune</code> Artisan command in your application's <code>routes/console.php</code> file. You are free to choose the appropriate interval at which this command should be run:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Support\Facades\</span><span style="color: #FFCB8B;">Schedule</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #FFCB8B;">Schedule</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">command</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">model:prune</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">daily</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use Illuminate\Support\Facades\Schedule;

Schedule::command(&#39;model:prune&#39;)-&gt;daily();</div></code></pre>
</div>
<p>Behind the scenes, the <code>model:prune</code> command will automatically detect &quot;Prunable&quot; models within your application's <code>app/Models</code> directory. If your models are in a different location, you may use the <code>--model</code> option to specify the model class names:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #FFCB8B;">Schedule</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">command</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">model:prune</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, [</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">--model</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> [</span><span style="color: #FFCB8B;">Address</span><span style="color: #89DDFF;">::</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;">, </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;">],</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">])</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">daily</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
Schedule::command(&#39;model:prune&#39;, [
    &#39;--model&#39; =&gt; [Address::class, Flight::class],
])-&gt;daily();</div></code></pre>
</div>
<p>If you wish to exclude certain models from being pruned while pruning all other detected models, you may use the <code>--except</code> option:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #FFCB8B;">Schedule</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">command</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">model:prune</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, [</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">--except</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> [</span><span style="color: #FFCB8B;">Address</span><span style="color: #89DDFF;">::</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;">, </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;">],</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">])</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">daily</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
Schedule::command(&#39;model:prune&#39;, [
    &#39;--except&#39; =&gt; [Address::class, Flight::class],
])-&gt;daily();</div></code></pre>
</div>
<p>You may test your <code>prunable</code> query by executing the <code>model:prune</code> command with the <code>--pretend</code> option. When pretending, the <code>model:prune</code> command will simply report how many records would be pruned if the command were to actually run:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="shell" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">model:prune</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">--pretend</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
php artisan model:prune --pretend</div></code></pre>
</div>
<div class="flex flex-col p-3 mb-10 space-y-4 text-base leading-normal border rounded-md lg:px-4 lg:flex-row lg:space-y-0 lg:space-x-4 border-sand-light-5 callout dark:border-sand-dark-5 dark:text-sand-light-3 text-sand-dark-3">
    <div class="w-8 h-8 p-2 lg:my-1.5 rounded-xs flex items-center justify-center shrink-0 bg-[#F53003]">
        <svg width="2" height="18" viewBox="0 0 2 18" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M1 17V16.99M1 1V13" stroke="#FDFDFC" stroke-width="2" stroke-linecap="square"/>
</svg>

    </div>
    <p class="callout text-pretty">
Soft deleting models will be permanently deleted (<code>forceDelete</code>) if they match the prunable query.</p>
</div>
<h4 id="mass-pruning"><a href="#mass-pruning">Mass Pruning</a></h4>
<p>When models are marked with the <code>Illuminate\Database\Eloquent\MassPrunable</code> trait, models are deleted from the database using mass-deletion queries. Therefore, the <code>pruning</code> method will not be invoked, nor will the <code>deleting</code> and <code>deleted</code> model events be dispatched. This is because the models are never actually retrieved before deletion, thus making the pruning process much more efficient:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Builder</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">MassPrunable</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">Flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">MassPrunable</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #697098;">     * Get the prunable model query.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">prunable</span><span style="color: #D9F5DD;">()</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Builder</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #BFC7D5;">    {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span><span style="color: #BFC7D5;">        </span><span style="color: #C792EA;">return</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">static</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">created_at</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">&lt;=</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #82AAFF;">now</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">minus</span><span style="color: #BFC7D5;">(months: </span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">));</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">19</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">20</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\MassPrunable;

class Flight extends Model
{
    use MassPrunable;

    /**
     * Get the prunable model query.
     */
    public function prunable(): Builder
    {
        return static::where(&#39;created_at&#39;, &#39;&lt;=&#39;, now()-&gt;minus(months: 1));
    }
}</div></code></pre>
</div>
<h2 id="replicating-models"><a href="#replicating-models">Replicating Models</a></h2>
<p>You may create an unsaved copy of an existing model instance using the <code>replicate</code> method. This method is particularly useful when you have model instances that share many of the same attributes:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">Address</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #BEC5D4;">$shipping</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Address</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">create</span><span style="color: #BFC7D5;">([</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">type</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">shipping</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">line_1</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">123 Example Street</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">city</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Victorville</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">state</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">CA</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">postcode</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">90001</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">]);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BEC5D4;">$billing</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$shipping</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">replicate</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">fill</span><span style="color: #BFC7D5;">([</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">type</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">billing</span><span style="color: #D9F5DD;">&#39;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #BFC7D5;">]);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BEC5D4;">$billing</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">save</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\Address;

$shipping = Address::create([
    &#39;type&#39; =&gt; &#39;shipping&#39;,
    &#39;line_1&#39; =&gt; &#39;123 Example Street&#39;,
    &#39;city&#39; =&gt; &#39;Victorville&#39;,
    &#39;state&#39; =&gt; &#39;CA&#39;,
    &#39;postcode&#39; =&gt; &#39;90001&#39;,
]);

$billing = $shipping-&gt;replicate()-&gt;fill([
    &#39;type&#39; =&gt; &#39;billing&#39;
]);

$billing-&gt;save();</div></code></pre>
</div>
<p>To exclude one or more attributes from being replicated to the new model, you may pass an array to the <code>replicate</code> method:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Flight</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">create</span><span style="color: #BFC7D5;">([</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">destination</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">LAX</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">origin</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">LHR</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">last_flown</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">2020-03-04 11:00:00</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">last_pilot_id</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #F78C6C;">747</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #BFC7D5;">]);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BEC5D4;">$flight</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$flight</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">replicate</span><span style="color: #BFC7D5;">([</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">last_flown</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">last_pilot_id</span><span style="color: #D9F5DD;">&#39;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BFC7D5;">]);</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$flight = Flight::create([
    &#39;destination&#39; =&gt; &#39;LAX&#39;,
    &#39;origin&#39; =&gt; &#39;LHR&#39;,
    &#39;last_flown&#39; =&gt; &#39;2020-03-04 11:00:00&#39;,
    &#39;last_pilot_id&#39; =&gt; 747,
]);

$flight = $flight-&gt;replicate([
    &#39;last_flown&#39;,
    &#39;last_pilot_id&#39;
]);</div></code></pre>
</div>
<h2 id="query-scopes"><a href="#query-scopes">Query Scopes</a></h2>
<h3 id="global-scopes"><a href="#global-scopes">Global Scopes</a></h3>
<p>Global scopes allow you to add constraints to all queries for a given model. Laravel's own <a href="#soft-deleting">soft delete</a> functionality utilizes global scopes to only retrieve &quot;non-deleted&quot; models from the database. Writing your own global scopes can provide a convenient, easy way to make sure every query for a given model receives certain constraints.</p>
<h4 id="generating-scopes"><a href="#generating-scopes">Generating Scopes</a></h4>
<p>To generate a new global scope, you may invoke the <code>make:scope</code> Artisan command, which will place the generated scope in your application's <code>app/Models/Scopes</code> directory:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="shell" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:scope</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">AncientScope</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
php artisan make:scope AncientScope</div></code></pre>
</div>
<h4 id="writing-global-scopes"><a href="#writing-global-scopes">Writing Global Scopes</a></h4>
<p>Writing a global scope is simple. First, use the <code>make:scope</code> command to generate a class that implements the <code>Illuminate\Database\Eloquent\Scope</code> interface. The <code>Scope</code> interface requires you to implement one method: <code>apply</code>. The <code>apply</code> method may add <code>where</code> constraints or other types of clauses to the query as needed:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models\Scopes;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Builder</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Scope</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">AncientScope</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">implements</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Scope</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #697098;">     * Apply the scope to a given Eloquent query builder.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">apply</span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">Builder</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$builder</span><span style="color: #BFC7D5;">, </span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$model</span><span style="color: #D9F5DD;">)</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">    {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #BFC7D5;">        </span><span style="color: #BEC5D4;">$builder</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">created_at</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">&lt;</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #82AAFF;">now</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">minus</span><span style="color: #BFC7D5;">(years: </span><span style="color: #F78C6C;">2000</span><span style="color: #BFC7D5;">));</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models\Scopes;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Scope;

class AncientScope implements Scope
{
    /**
     *Apply the scope to a given Eloquent query builder.
     */
    public function apply(Builder $builder, Model $model): void
    {
        $builder-&gt;where(&#39;created_at&#39;, &#39;&lt;&#39;, now()-&gt;minus(years: 2000));
    }
}</div></code></pre>
</div>
<div class="flex flex-col p-3 mb-10 space-y-4 text-base leading-normal border rounded-md lg:px-4 lg:flex-row lg:space-y-0 lg:space-x-4 border-sand-light-5 callout dark:border-sand-dark-5 dark:text-sand-light-3 text-sand-dark-3">
    <div class="w-8 h-8 p-2 lg:my-1.5 rounded-xs flex items-center justify-center shrink-0 bg-[#8D54C5]">
        <svg width="16" height="21" viewBox="0 0 16 21" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M5 20H11M5.5 14H10.5M15 8C15 4.13401 11.866 1 8 1C4.13401 1 1 4.13401 1 8C1 10.7924 2.63505 13.2029 5 14.3264V17H11V14.3264C13.3649 13.2029 15 10.7924 15 8Z" stroke="#FDFDFC" stroke-width="1.5" stroke-linecap="square"/>
</svg>

    </div>
    <p class="callout text-pretty">
If your global scope is adding columns to the select clause of the query, you should use the <code>addSelect</code> method instead of <code>select</code>. This will prevent the unintentional replacement of the query's existing select clause.</p>
</div>
<h4 id="applying-global-scopes"><a href="#applying-global-scopes">Applying Global Scopes</a></h4>
<p>To assign a global scope to a model, you may simply place the <code>ScopedBy</code> attribute on the model:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\Scopes\</span><span style="color: #FFCB8B;">AncientScope</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\Attributes\</span><span style="color: #FFCB8B;">ScopedBy</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BFC7D5;">#[ScopedBy([</span><span style="color: #FFCB8B;">AncientScope</span><span style="color: #89DDFF;">::</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;">])]</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">User</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">//</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use App\Models\Scopes\AncientScope;
use Illuminate\Database\Eloquent\Attributes\ScopedBy;

# [ScopedBy([AncientScope::class])]
class User extends Model
{
    //
}</div></code></pre>
</div>
<p>Or, you may manually register the global scope by overriding the model's <code>booted</code> method and invoke the model's <code>addGlobalScope</code> method. The <code>addGlobalScope</code> method accepts an instance of your scope as its only argument:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\Scopes\</span><span style="color: #FFCB8B;">AncientScope</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">User</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #697098;">     * The &quot;booted&quot; method of the model.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">static</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">booted</span><span style="color: #D9F5DD;">()</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">    {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">        </span><span style="color: #C792EA;">static</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">addGlobalScope</span><span style="color: #BFC7D5;">(</span><span style="color: #89DDFF;">new</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">AncientScope</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use App\Models\Scopes\AncientScope;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     *The &quot;booted&quot; method of the model.
     */
    protected static function booted(): void
    {
        static::addGlobalScope(new AncientScope);
    }
}</div></code></pre>
</div>
<p>After adding the scope in the example above to the <code>App\Models\User</code> model, a call to the <code>User::all()</code> method will execute the following SQL query:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="sql" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">select</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">*</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">from</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">`</span><span style="color: #C3E88D;">users</span><span style="color: #D9F5DD;">`</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">where</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">`</span><span style="color: #C3E88D;">created_at</span><span style="color: #D9F5DD;">`</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">&lt;</span><span style="color: #BFC7D5;"> </span><span style="color: #F78C6C;">0021</span><span style="color: #89DDFF;">-</span><span style="color: #F78C6C;">02</span><span style="color: #89DDFF;">-</span><span style="color: #F78C6C;">18</span><span style="color: #BFC7D5;"> </span><span style="color: #F78C6C;">00</span><span style="color: #BFC7D5;">:</span><span style="color: #F78C6C;">00</span><span style="color: #BFC7D5;">:</span><span style="color: #F78C6C;">00</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
select * from `users` where `created_at` &lt; 0021-02-18 00:00:00</div></code></pre>
</div>
<h4 id="anonymous-global-scopes"><a href="#anonymous-global-scopes">Anonymous Global Scopes</a></h4>
<p>Eloquent also allows you to define global scopes using closures, which is particularly useful for simple scopes that do not warrant a separate class of their own. When defining a global scope using a closure, you should provide a scope name of your own choosing as the first argument to the <code>addGlobalScope</code> method:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Builder</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">User</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #697098;">     * The &quot;booted&quot; method of the model.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">static</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">booted</span><span style="color: #D9F5DD;">()</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">    {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">        </span><span style="color: #C792EA;">static</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">addGlobalScope</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">ancient</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">Builder</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$builder</span><span style="color: #D9F5DD;">)</span><span style="color: #BFC7D5;"> {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #BFC7D5;">            </span><span style="color: #BEC5D4;">$builder</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">created_at</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">&lt;</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #82AAFF;">now</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">minus</span><span style="color: #BFC7D5;">(years: </span><span style="color: #F78C6C;">2000</span><span style="color: #BFC7D5;">));</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #BFC7D5;">        });</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">19</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     *The &quot;booted&quot; method of the model.
     */
    protected static function booted(): void
    {
        static::addGlobalScope(&#39;ancient&#39;, function (Builder $builder) {
            $builder-&gt;where(&#39;created_at&#39;, &#39;&lt;&#39;, now()-&gt;minus(years: 2000));
        });
    }
}</div></code></pre>
</div>
<h4 id="removing-global-scopes"><a href="#removing-global-scopes">Removing Global Scopes</a></h4>
<p>If you would like to remove a global scope for a given query, you may use the <code>withoutGlobalScope</code> method. This method accepts the class name of the global scope as its only argument:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">withoutGlobalScope</span><span style="color: #BFC7D5;">(</span><span style="color: #FFCB8B;">AncientScope</span><span style="color: #89DDFF;">::</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">get</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
User::withoutGlobalScope(AncientScope::class)-&gt;get();</div></code></pre>
</div>
<p>Or, if you defined the global scope using a closure, you should pass the string name that you assigned to the global scope:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">withoutGlobalScope</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">ancient</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">get</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
User::withoutGlobalScope(&#39;ancient&#39;)-&gt;get();</div></code></pre>
</div>
<p>If you would like to remove several or even all of the query's global scopes, you may use the <code>withoutGlobalScopes</code> and <code>withoutGlobalScopesExcept</code> methods:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #697098;">//</span><span style="color: #697098;"> Remove all of the global scopes...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">withoutGlobalScopes</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">get</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span><span style="color: #697098;">//</span><span style="color: #697098;"> Remove some of the global scopes...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">withoutGlobalScopes</span><span style="color: #BFC7D5;">([</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #BFC7D5;">    </span><span style="color: #FFCB8B;">FirstScope</span><span style="color: #89DDFF;">::</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;">, </span><span style="color: #FFCB8B;">SecondScope</span><span style="color: #89DDFF;">::</span><span style="color: #C792EA;">class</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #BFC7D5;">])</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">get</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #697098;">//</span><span style="color: #697098;"> Remove all global scopes except the given ones...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">withoutGlobalScopesExcept</span><span style="color: #BFC7D5;">([</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BFC7D5;">    </span><span style="color: #FFCB8B;">SecondScope</span><span style="color: #89DDFF;">::</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #BFC7D5;">])</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">get</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
// Remove all of the global scopes...
User::withoutGlobalScopes()-&gt;get();

// Remove some of the global scopes...
User::withoutGlobalScopes([
    FirstScope::class, SecondScope::class
])-&gt;get();

// Remove all global scopes except the given ones...
User::withoutGlobalScopesExcept([
    SecondScope::class,
])-&gt;get();</div></code></pre>
</div>
<h3 id="local-scopes"><a href="#local-scopes">Local Scopes</a></h3>
<p>Local scopes allow you to define common sets of query constraints that you may easily re-use throughout your application. For example, you may need to frequently retrieve all users that are considered &quot;popular&quot;. To define a scope, add the <code>Scope</code> attribute to an Eloquent method.</p>
<p>Scopes should always return the same query builder instance or <code>void</code>:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\Attributes\</span><span style="color: #FFCB8B;">Scope</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Builder</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">User</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #697098;">     * Scope a query to only include popular users.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">    #[Scope]</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">popular</span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">Builder</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$query</span><span style="color: #D9F5DD;">)</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #BFC7D5;">    {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #BFC7D5;">        </span><span style="color: #BEC5D4;">$query</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">votes</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">&gt;</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">100</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">19</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">20</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">21</span><span style="color: #697098;">     * Scope a query to only include active users.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">22</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">23</span><span style="color: #BFC7D5;">    #[Scope]</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">24</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">active</span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">Builder</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$query</span><span style="color: #D9F5DD;">)</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">25</span><span style="color: #BFC7D5;">    {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">26</span><span style="color: #BFC7D5;">        </span><span style="color: #BEC5D4;">$query</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">active</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">27</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">28</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Scope;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     *Scope a query to only include popular users.
     */
    #[Scope]
    protected function popular(Builder $query): void
    {
        $query-&gt;where(&#39;votes&#39;, &#39;&gt;&#39;, 100);
    }

    /**
     * Scope a query to only include active users.
     */
    #[Scope]
    protected function active(Builder $query): void
    {
        $query-&gt;where(&#39;active&#39;, 1);
    }
}</div></code></pre>
</div>
<h4 id="utilizing-a-local-scope"><a href="#utilizing-a-local-scope">Utilizing a Local Scope</a></h4>
<p>Once the scope has been defined, you may call the scope methods when querying the model. You can even chain calls to various scopes:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">User</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BEC5D4;">$users</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">popular</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">active</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">orderBy</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">created_at</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">get</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\User;

$users = User::popular()-&gt;active()-&gt;orderBy(&#39;created_at&#39;)-&gt;get();</div></code></pre>
</div>
<p>Combining multiple Eloquent model scopes via an <code>or</code> query operator may require the use of closures to achieve the correct <a href="/docs/12.x/queries#logical-grouping">logical grouping</a>:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$users</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">popular</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">orWhere</span><span style="color: #BFC7D5;">(</span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">Builder</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$query</span><span style="color: #D9F5DD;">)</span><span style="color: #BFC7D5;"> {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #BEC5D4;">$query</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">active</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">})</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">get</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$users = User::popular()-&gt;orWhere(function (Builder $query) {
    $query-&gt;active();
})-&gt;get();</div></code></pre>
</div>
<p>However, since this can be cumbersome, Laravel provides a &quot;higher order&quot; <code>orWhere</code> method that allows you to fluently chain scopes together without the use of closures:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$users</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">popular</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;orWhere-&gt;</span><span style="color: #82AAFF;">active</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">get</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$users = User::popular()-&gt;orWhere-&gt;active()-&gt;get();</div></code></pre>
</div>
<h4 id="dynamic-scopes"><a href="#dynamic-scopes">Dynamic Scopes</a></h4>
<p>Sometimes you may wish to define a scope that accepts parameters. To get started, just add your additional parameters to your scope method's signature. Scope parameters should be defined after the <code>$query</code> parameter:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\Attributes\</span><span style="color: #FFCB8B;">Scope</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Builder</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">User</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #697098;">     * Scope a query to only include users of a given type.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">    #[Scope]</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">ofType</span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">Builder</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$query</span><span style="color: #BFC7D5;">, </span><span style="color: #C792EA;">string</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$type</span><span style="color: #D9F5DD;">)</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #BFC7D5;">    {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #BFC7D5;">        </span><span style="color: #BEC5D4;">$query</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">where</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">type</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">, </span><span style="color: #BEC5D4;">$type</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">19</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Scope;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     *Scope a query to only include users of a given type.
     */
    #[Scope]
    protected function ofType(Builder $query, string $type): void
    {
        $query-&gt;where(&#39;type&#39;, $type);
    }
}</div></code></pre>
</div>
<p>Once the expected arguments have been added to your scope method's signature, you may pass the arguments when calling the scope:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$users</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">ofType</span><span style="color: #BFC7D5;">(</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">admin</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">get</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$users = User::ofType(&#39;admin&#39;)-&gt;get();</div></code></pre>
</div>
<h3 id="pending-attributes"><a href="#pending-attributes">Pending Attributes</a></h3>
<p>If you would like to use scopes to create models that have the same attributes as those used to constrain the scope, you may use the <code>withAttributes</code> method when building the scope query:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\Attributes\</span><span style="color: #FFCB8B;">Scope</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Builder</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">Post</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #697098;">     * Scope the query to only include drafts.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">    #[Scope]</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">draft</span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">Builder</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$query</span><span style="color: #D9F5DD;">)</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #BFC7D5;">    {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #BFC7D5;">        </span><span style="color: #BEC5D4;">$query</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">withAttributes</span><span style="color: #BFC7D5;">([</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span><span style="color: #BFC7D5;">            </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">hidden</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">true</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">19</span><span style="color: #BFC7D5;">        ]);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">20</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">21</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Scope;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;

class Post extends Model
{
    /**
     *Scope the query to only include drafts.
     */
    #[Scope]
    protected function draft(Builder $query): void
    {
        $query-&gt;withAttributes([
            &#39;hidden&#39; =&gt; true,
        ]);
    }
}</div></code></pre>
</div>
<p>The <code>withAttributes</code> method will add <code>where</code> conditions to the query using the given attributes, and it will also add the given attributes to any models created via the scope:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$draft</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Post</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">draft</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">create</span><span style="color: #BFC7D5;">([</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">title</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">In Progress</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">]);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BEC5D4;">$draft</span><span style="color: #89DDFF;">-&gt;hidden</span><span style="color: #BFC7D5;">; </span><span style="color: #697098;">//</span><span style="color: #697098;"> true</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$draft = Post::draft()-&gt;create([&#39;title&#39; =&gt; &#39;In Progress&#39;]);

$draft-&gt;hidden; // true</div></code></pre>
</div>
<p>To instruct the <code>withAttributes</code> method to not add <code>where</code> conditions to the query, you may set the <code>asConditions</code> argument to <code>false</code>:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$query</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">withAttributes</span><span style="color: #BFC7D5;">([</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">hidden</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">true</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">], asConditions: </span><span style="color: #82AAFF;">false</span><span style="color: #BFC7D5;">);</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$query-&gt;withAttributes([
    &#39;hidden&#39; =&gt; true,
], asConditions: false);</div></code></pre>
</div>
<h2 id="comparing-models"><a href="#comparing-models">Comparing Models</a></h2>
<p>Sometimes you may need to determine if two models are the &quot;same&quot; or not. The <code>is</code> and <code>isNot</code> methods may be used to quickly verify two models have the same primary key, table, and database connection or not:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">if</span><span style="color: #BFC7D5;"> (</span><span style="color: #BEC5D4;">$post</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">is</span><span style="color: #BFC7D5;">(</span><span style="color: #BEC5D4;">$anotherPost</span><span style="color: #BFC7D5;">)) {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">}</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #C792EA;">if</span><span style="color: #BFC7D5;"> (</span><span style="color: #BEC5D4;">$post</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">isNot</span><span style="color: #BFC7D5;">(</span><span style="color: #BEC5D4;">$anotherPost</span><span style="color: #BFC7D5;">)) {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">7</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
if ($post-&gt;is($anotherPost)) {
    // ...
}

if ($post-&gt;isNot($anotherPost)) {
    // ...
}</div></code></pre>
</div>
<p>The <code>is</code> and <code>isNot</code> methods are also available when using the <code>belongsTo</code>, <code>hasOne</code>, <code>morphTo</code>, and <code>morphOne</code> <a href="/docs/12.x/eloquent-relationships">relationships</a>. This method is particularly helpful when you would like to compare a related model without issuing a query to retrieve that model:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">if</span><span style="color: #BFC7D5;"> (</span><span style="color: #BEC5D4;">$post</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">author</span><span style="color: #BFC7D5;">()</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">is</span><span style="color: #BFC7D5;">(</span><span style="color: #BEC5D4;">$user</span><span style="color: #BFC7D5;">)) {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
if ($post-&gt;author()-&gt;is($user)) {
    // ...
}</div></code></pre>
</div>
<h2 id="events"><a href="#events">Events</a></h2>
<div class="flex flex-col p-3 mb-10 space-y-4 text-base leading-normal border rounded-md lg:px-4 lg:flex-row lg:space-y-0 lg:space-x-4 border-sand-light-5 callout dark:border-sand-dark-5 dark:text-sand-light-3 text-sand-dark-3">
    <div class="w-8 h-8 p-2 lg:my-1.5 rounded-xs flex items-center justify-center shrink-0 bg-[#8D54C5]">
        <svg width="16" height="21" viewBox="0 0 16 21" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M5 20H11M5.5 14H10.5M15 8C15 4.13401 11.866 1 8 1C4.13401 1 1 4.13401 1 8C1 10.7924 2.63505 13.2029 5 14.3264V17H11V14.3264C13.3649 13.2029 15 10.7924 15 8Z" stroke="#FDFDFC" stroke-width="1.5" stroke-linecap="square"/>
</svg>

    </div>
    <p class="callout text-pretty">
Want to broadcast your Eloquent events directly to your client-side application? Check out Laravel's <a href="/docs/12.x/broadcasting#model-broadcasting">model event broadcasting</a>.</p>
</div>
<p>Eloquent models dispatch several events, allowing you to hook into the following moments in a model's lifecycle: <code>retrieved</code>, <code>creating</code>, <code>created</code>, <code>updating</code>, <code>updated</code>, <code>saving</code>, <code>saved</code>, <code>deleting</code>, <code>deleted</code>, <code>trashed</code>, <code>forceDeleting</code>, <code>forceDeleted</code>, <code>restoring</code>, <code>restored</code>, and <code>replicating</code>.</p>
<p>The <code>retrieved</code> event will dispatch when an existing model is retrieved from the database. When a new model is saved for the first time, the <code>creating</code> and <code>created</code> events will dispatch. The <code>updating</code> / <code>updated</code> events will dispatch when an existing model is modified and the <code>save</code> method is called. The <code>saving</code> / <code>saved</code> events will dispatch when a model is created or updated - even if the model's attributes have not been changed. Event names ending with <code>-ing</code> are dispatched before any changes to the model are persisted, while events ending with <code>-ed</code> are dispatched after the changes to the model are persisted.</p>
<p>To start listening to model events, define a <code>$dispatchesEvents</code> property on your Eloquent model. This property maps various points of the Eloquent model's lifecycle to your own <a href="/docs/12.x/events">event classes</a>. Each model event class should expect to receive an instance of the affected model via its constructor:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Events\</span><span style="color: #FFCB8B;">UserDeleted</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Events\</span><span style="color: #FFCB8B;">UserSaved</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Foundation\Auth\</span><span style="color: #FFCB8B;">User</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">as</span><span style="color: #BFC7D5;"> Authenticatable;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Notifications\</span><span style="color: #FFCB8B;">Notifiable</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">User</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Authenticatable</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">Notifiable</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #697098;">     * The event map for the model.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #697098;">     *</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #697098;">     * </span><span style="color: #C792EA;">@var</span><span style="color: #697098;"> </span><span style="color: #C792EA;">array</span><span style="color: #697098;">&lt;</span><span style="color: #C792EA;">string</span><span style="color: #697098;">, string&gt;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">19</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$dispatchesEvents</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> [</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">20</span><span style="color: #BFC7D5;">        </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">saved</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">UserSaved</span><span style="color: #89DDFF;">::</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">21</span><span style="color: #BFC7D5;">        </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">deleted</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;"> </span><span style="color: #89DDFF;">=&gt;</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">UserDeleted</span><span style="color: #89DDFF;">::</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;">,</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">22</span><span style="color: #BFC7D5;">    ];</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">23</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use App\Events\UserDeleted;
use App\Events\UserSaved;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;

class User extends Authenticatable
{
    use Notifiable;

    /**
     * The event map for the model.
     *
     * @var array&lt;string, string&gt;
     */
    protected $dispatchesEvents = [
        &#39;saved&#39; =&gt; UserSaved::class,
        &#39;deleted&#39; =&gt; UserDeleted::class,
    ];
}</div></code></pre>
</div>
<p>After defining and mapping your Eloquent events, you may use <a href="/docs/12.x/events#defining-listeners">event listeners</a> to handle the events.</p>
<div class="flex flex-col p-3 mb-10 space-y-4 text-base leading-normal border rounded-md lg:px-4 lg:flex-row lg:space-y-0 lg:space-x-4 border-sand-light-5 callout dark:border-sand-dark-5 dark:text-sand-light-3 text-sand-dark-3">
    <div class="w-8 h-8 p-2 lg:my-1.5 rounded-xs flex items-center justify-center shrink-0 bg-[#F53003]">
        <svg width="2" height="18" viewBox="0 0 2 18" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M1 17V16.99M1 1V13" stroke="#FDFDFC" stroke-width="2" stroke-linecap="square"/>
</svg>

    </div>
    <p class="callout text-pretty">
When issuing a mass update or delete query via Eloquent, the <code>saved</code>, <code>updated</code>, <code>deleting</code>, and <code>deleted</code> model events will not be dispatched for the affected models. This is because the models are never actually retrieved when performing mass updates or deletes.</p>
</div>
<h3 id="events-using-closures"><a href="#events-using-closures">Using Closures</a></h3>
<p>Instead of using custom event classes, you may register closures that execute when various model events are dispatched. Typically, you should register these closures in the <code>booted</code> method of your model:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Models;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\</span><span style="color: #FFCB8B;">Model</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">User</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Model</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #697098;">     * The &quot;booted&quot; method of the model.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">protected</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">static</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">booted</span><span style="color: #D9F5DD;">()</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #BFC7D5;">    {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">        </span><span style="color: #C792EA;">static</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">created</span><span style="color: #BFC7D5;">(</span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">User</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$user</span><span style="color: #D9F5DD;">)</span><span style="color: #BFC7D5;"> {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">            </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #BFC7D5;">        });</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     *The &quot;booted&quot; method of the model.
     */
    protected static function booted(): void
    {
        static::created(function (User $user) {
            // ...
        });
    }
}</div></code></pre>
</div>
<p>If needed, you may utilize <a href="/docs/12.x/events#queuable-anonymous-event-listeners">queueable anonymous event listeners</a> when registering model events. This will instruct Laravel to execute the model event listener in the background using your application's <a href="/docs/12.x/queues">queue</a>:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> Illuminate\Events\</span><span style="color: #FFCB8B;">queueable</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #C792EA;">static</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">created</span><span style="color: #BFC7D5;">(</span><span style="color: #82AAFF;">queueable</span><span style="color: #BFC7D5;">(</span><span style="color: #C792EA;">function</span><span style="color: #82AAFF;"> </span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">User</span><span style="color: #82AAFF;"> </span><span style="color: #BFC7D5;">$</span><span style="color: #BEC5D4;">user</span><span style="color: #D9F5DD;">)</span><span style="color: #82AAFF;"> </span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">    //</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BFC7D5;">}));</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use function Illuminate\Events\queueable;

static::created(queueable(function (User $user) {
    // ...
}));</div></code></pre>
</div>
<h3 id="observers"><a href="#observers">Observers</a></h3>
<h4 id="defining-observers"><a href="#defining-observers">Defining Observers</a></h4>
<p>If you are listening for many events on a given model, you may use observers to group all of your listeners into a single class. Observer classes have method names which reflect the Eloquent events you wish to listen for. Each of these methods receives the affected model as their only argument. The <code>make:observer</code> Artisan command is the easiest way to create a new observer class:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="shell" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BFC7D5;">php </span><span style="color: #BFC7D5;">artisan</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">make:observer</span><span style="color: #BFC7D5;"> </span><span style="color: #BFC7D5;">UserObserver</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">--model=User</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
php artisan make:observer UserObserver --model=User</div></code></pre>
</div>
<p>This command will place the new observer in your <code>app/Observers</code> directory. If this directory does not exist, Artisan will create it for you. Your fresh observer will look like the following:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Observers;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">User</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">UserObserver</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #697098;">     * Handle the User &quot;created&quot; event.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">created</span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">User</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$user</span><span style="color: #D9F5DD;">)</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #BFC7D5;">    {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">        </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">18</span><span style="color: #697098;">     * Handle the User &quot;updated&quot; event.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">19</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">20</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">updated</span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">User</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$user</span><span style="color: #D9F5DD;">)</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">21</span><span style="color: #BFC7D5;">    {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">22</span><span style="color: #BFC7D5;">        </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">23</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">24</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">25</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">26</span><span style="color: #697098;">     * Handle the User &quot;deleted&quot; event.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">27</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">28</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">deleted</span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">User</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$user</span><span style="color: #D9F5DD;">)</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">29</span><span style="color: #BFC7D5;">    {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">30</span><span style="color: #BFC7D5;">        </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">31</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">32</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">33</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">34</span><span style="color: #697098;">     * Handle the User &quot;restored&quot; event.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">35</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">36</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">restored</span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">User</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$user</span><span style="color: #D9F5DD;">)</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">37</span><span style="color: #BFC7D5;">    {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">38</span><span style="color: #BFC7D5;">        </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">39</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">40</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">41</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">42</span><span style="color: #697098;">     * Handle the User &quot;forceDeleted&quot; event.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">43</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">44</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">forceDeleted</span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">User</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$user</span><span style="color: #D9F5DD;">)</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">45</span><span style="color: #BFC7D5;">    {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">46</span><span style="color: #BFC7D5;">        </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">47</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">48</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Observers;

use App\Models\User;

class UserObserver
{
    /**
     *Handle the User &quot;created&quot; event.
     */
    public function created(User $user): void
    {
        // ...
    }

    /**
     * Handle the User &quot;updated&quot; event.
     */
    public function updated(User $user): void
    {
        // ...
    }

    /**
     * Handle the User &quot;deleted&quot; event.
     */
    public function deleted(User $user): void
    {
        // ...
    }

    /**
     * Handle the User &quot;restored&quot; event.
     */
    public function restored(User $user): void
    {
        // ...
    }

    /**
     * Handle the User &quot;forceDeleted&quot; event.
     */
    public function forceDeleted(User $user): void
    {
        // ...
    }
}</div></code></pre>
</div>
<p>To register an observer, you may place the <code>ObservedBy</code> attribute on the corresponding model:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Observers\</span><span style="color: #FFCB8B;">UserObserver</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Database\Eloquent\Attributes\</span><span style="color: #FFCB8B;">ObservedBy</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">#[ObservedBy([</span><span style="color: #FFCB8B;">UserObserver</span><span style="color: #89DDFF;">::</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;">])]</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">User</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">extends</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">Authenticatable</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">7</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">//</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">8</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Observers\UserObserver;
use Illuminate\Database\Eloquent\Attributes\ObservedBy;

# [ObservedBy([UserObserver::class])]
class User extends Authenticatable
{
    //
}</div></code></pre>
</div>
<p>Or, you may manually register an observer by invoking the <code>observe</code> method on the model you wish to observe. You may register observers in the <code>boot</code> method of your application's <code>AppServiceProvider</code> class:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">User</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Observers\</span><span style="color: #FFCB8B;">UserObserver</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #697098;"> * Bootstrap any application services.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #697098;"> </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">boot</span><span style="color: #D9F5DD;">()</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">    </span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">observe</span><span style="color: #BFC7D5;">(</span><span style="color: #FFCB8B;">UserObserver</span><span style="color: #89DDFF;">::</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\User;
use App\Observers\UserObserver;

/**

* Bootstrap any application services.
 */
public function boot(): void
{
    User::observe(UserObserver::class);
}</div></code></pre>

</div>
<div class="flex flex-col p-3 mb-10 space-y-4 text-base leading-normal border rounded-md lg:px-4 lg:flex-row lg:space-y-0 lg:space-x-4 border-sand-light-5 callout dark:border-sand-dark-5 dark:text-sand-light-3 text-sand-dark-3">
    <div class="w-8 h-8 p-2 lg:my-1.5 rounded-xs flex items-center justify-center shrink-0 bg-[#8D54C5]">
        <svg width="16" height="21" viewBox="0 0 16 21" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M5 20H11M5.5 14H10.5M15 8C15 4.13401 11.866 1 8 1C4.13401 1 1 4.13401 1 8C1 10.7924 2.63505 13.2029 5 14.3264V17H11V14.3264C13.3649 13.2029 15 10.7924 15 8Z" stroke="#FDFDFC" stroke-width="1.5" stroke-linecap="square"/>
</svg>

    </div>
    <p class="callout text-pretty">
There are additional events an observer can listen to, such as <code>saving</code> and <code>retrieved</code>. These events are described within the <a href="#events">events</a> documentation.</p>
</div>
<h4 id="observers-and-database-transactions"><a href="#observers-and-database-transactions">Observers and Database Transactions</a></h4>
<p>When models are being created within a database transaction, you may want to instruct an observer to only execute its event handlers after the database transaction is committed. You may accomplish this by implementing the <code>ShouldHandleEventsAfterCommit</code> interface on your observer. If a database transaction is not in progress, the event handlers will execute immediately:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 1</span><span style="color: #D3423E;">&lt;?php</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 3</span><span style="color: #C792EA;">namespace</span><span style="color: #BFC7D5;"> App\Observers;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 5</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">User</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 6</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> Illuminate\Contracts\Events\</span><span style="color: #FFCB8B;">ShouldHandleEventsAfterCommit</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 7</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 8</span><span style="color: #C792EA;">class</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB6B;">UserObserver</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">implements</span><span style="color: #BFC7D5;"> </span><span style="color: #A9C77D;">ShouldHandleEventsAfterCommit</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number"> 9</span><span style="color: #BFC7D5;">{</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">10</span><span style="color: #BFC7D5;">    </span><span style="color: #697098;">/**</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">11</span><span style="color: #697098;">     * Handle the User &quot;created&quot; event.</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">12</span><span style="color: #697098;">     </span><span style="color: #697098;">*/</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">13</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">public</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #82AAFF;">created</span><span style="color: #D9F5DD;">(</span><span style="color: #FFCB8B;">User</span><span style="color: #BFC7D5;"> </span><span style="color: #BEC5D4;">$user</span><span style="color: #D9F5DD;">)</span><span style="color: #89DDFF;">:</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">void</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">14</span><span style="color: #BFC7D5;">    {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">15</span><span style="color: #BFC7D5;">        </span><span style="color: #697098;">//</span><span style="color: #697098;"> ...</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">16</span><span style="color: #BFC7D5;">    }</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">17</span><span style="color: #BFC7D5;">}</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
&lt;?php

namespace App\Observers;

use App\Models\User;
use Illuminate\Contracts\Events\ShouldHandleEventsAfterCommit;

class UserObserver implements ShouldHandleEventsAfterCommit
{
    /**
     *Handle the User &quot;created&quot; event.
     */
    public function created(User $user): void
    {
        // ...
    }
}</div></code></pre>
</div>
<h3 id="muting-events"><a href="#muting-events">Muting Events</a></h3>
<p>You may occasionally need to temporarily &quot;mute&quot; all events fired by a model. You may achieve this using the <code>withoutEvents</code> method. The <code>withoutEvents</code> method accepts a closure as its only argument. Any code executed within this closure will not dispatch model events, and any value returned by the closure will be returned by the <code>withoutEvents</code> method:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #C792EA;">use</span><span style="color: #BFC7D5;"> App\Models\</span><span style="color: #FFCB8B;">User</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BEC5D4;">$user</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">withoutEvents</span><span style="color: #BFC7D5;">(</span><span style="color: #C792EA;">function</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">()</span><span style="color: #BFC7D5;"> {</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span><span style="color: #BFC7D5;">    </span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">findOrFail</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">)</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">delete</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">6</span><span style="color: #BFC7D5;">    </span><span style="color: #C792EA;">return</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">find</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">2</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">7</span><span style="color: #BFC7D5;">});</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
use App\Models\User;

$user = User::withoutEvents(function () {
    User::findOrFail(1)-&gt;delete();

    return User::find(2);
});</div></code></pre>
</div>
<h4 id="saving-a-single-model-without-events"><a href="#saving-a-single-model-without-events">Saving a Single Model Without Events</a></h4>
<p>Sometimes you may wish to &quot;save&quot; a given model without dispatching any events. You may accomplish this using the <code>saveQuietly</code> method:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$user</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #FFCB8B;">User</span><span style="color: #89DDFF;">::</span><span style="color: #82AAFF;">findOrFail</span><span style="color: #BFC7D5;">(</span><span style="color: #F78C6C;">1</span><span style="color: #BFC7D5;">);</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;name</span><span style="color: #BFC7D5;"> </span><span style="color: #C792EA;">=</span><span style="color: #BFC7D5;"> </span><span style="color: #D9F5DD;">&#39;</span><span style="color: #C3E88D;">Victoria Faith</span><span style="color: #D9F5DD;">&#39;</span><span style="color: #BFC7D5;">;</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">4</span>&nbsp;</div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">5</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">saveQuietly</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$user = User::findOrFail(1);

$user-&gt;name = &#39;Victoria Faith&#39;;

$user-&gt;saveQuietly();</div></code></pre>
</div>
<p>You may also &quot;update&quot;, &quot;delete&quot;, &quot;soft delete&quot;, &quot;restore&quot;, and &quot;replicate&quot; a given model without dispatching any events:</p>
<div class="code-container">
<pre><code data-theme="olaolu-palenight" data-lang="php" class='torchlight' style='background-color: #292D3E; --theme-selection-background: #7580B850;'><!-- Syntax highlighted by torchlight.dev --><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">1</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">deleteQuietly</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">2</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">forceDeleteQuietly</span><span style="color: #BFC7D5;">();</span></div><div class='line'><span style="color:#4c5374; text-align: right; -webkit-user-select: none; user-select: none;" class="line-number">3</span><span style="color: #BEC5D4;">$user</span><span style="color: #89DDFF;">-&gt;</span><span style="color: #82AAFF;">restoreQuietly</span><span style="color: #BFC7D5;">();</span></div><div aria-hidden='true' hidden tabindex='-1' style='display: none;' class='torchlight-copy-target'>
$user-&gt;deleteQuietly();
$user-&gt;forceDeleteQuietly();
$user-&gt;restoreQuietly();</div></code></pre>
</div>
</div>
                            </section>
                        </section>
                    </div>
                </section>

                <div
                    class="relative col-span-12 hidden lg:col-span-9 lg:col-start-4 lg:pb-10 xl:col-span-3 xl:col-start-auto xl:block"
                >
                    <div class="relative pl-10 lg:sticky lg:top-28">
                        <div>
            <div class="flex flex-col items-start gap-4 text-xs">
    <button
        x-data="copyAsMarkdown('https://laravel.com/docs/12.x/eloquent.md')"
        @click.prevent="copy"
        :disabled="recentlyCopied"
        class="group inline-flex items-center gap-2 text-xs font-medium text-sand-light-11 not-disabled:hover:text-sand-light-12 dark:text-sand-dark-11 dark:not-disabled:hover:text-sand-dark-12"
    >
        <template x-if="recentlyCopied">
            <svg class="inline-block size-4 text-sand-light-9 group-not-disabled:group-hover:text-sand-light-12 dark:text-sand-dark-11 dark:group-not-disabled:group-hover:text-sand-dark-12"
    width="20"
    height="20"
    alt="Check icon"
    viewBox="0 0 20 20"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
>
    <path
        d="M5 11.6471L8.52941 14L15 6"
        stroke="currentColor"
        stroke-linecap="square"
    />
</svg>        </template>

        <template x-if="!recentlyCopied">
            <svg class="inline-block size-4 text-sand-light-9 group-not-disabled:group-hover:text-sand-light-12 dark:text-sand-dark-11 dark:group-not-disabled:group-hover:text-sand-dark-12" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M5.83301 5.83325V1.83325H14.1663V10.1666H10.1663" stroke="currentColor" stroke-width="1.25" stroke-linecap="square"/><path d="M1.83301 5.83325H10.1663V14.1666H1.83301V5.83325Z" stroke="currentColor" stroke-width="1.25" stroke-linecap="square"/></svg>        </template>

        <span x-text="recentlyCopied ? 'Copied' : 'Copy as markdown'">Copy as markdown</span>
    </button>
</div>

            <h3
            class="mt-9 mb-3 flex items-center gap-2 text-sm font-medium text-sand-light-11 dark:text-sand-dark-11"
        >
            <svg class="inline-block size-4 text-sand-light-9 dark:text-sand-dark-11" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M1.83301 7.99992H14.1663M1.83301 3.83325H14.1663M1.83301 12.1666H7.66634" stroke="#C8C7C1" stroke-width="1.25" stroke-linecap="square"/></svg>            On this page
        </h3>
    
    <div class="clean-scrollbar max-h-[calc(100vh-140px)] space-y-10 overflow-y-auto pb-10">
                    <div id="on-this-page-content" class="border-l border-sand-light-5 pr-4 dark:border-sand-dark-5">
                                    <ul class="space-y-1">
            <li class="mt-1.5 py-0.5 first:mt-0">
            <a
                href="#introduction"
                class="inline-block border-l-[3px] border-transparent pl-4 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
            >
                Introduction
            </a>

                    </li>
            <li class="mt-1.5 py-0.5 first:mt-0">
            <a
                href="#generating-model-classes"
                class="inline-block border-l-[3px] border-transparent pl-4 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
            >
                Generating Model Classes
            </a>

                    </li>
            <li class="mt-1.5 py-0.5 first:mt-0">
            <a
                href="#eloquent-model-conventions"
                class="inline-block border-l-[3px] border-transparent pl-4 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
            >
                Eloquent Model Conventions
            </a>

                            <ul class="mt-1.5">
                                            <li class="py-0.5">
                            <a
                                href="#table-names"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Table Names
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#primary-keys"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Primary Keys
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#uuid-and-ulid-keys"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                UUID and ULID Keys
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#timestamps"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Timestamps
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#database-connections"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Database Connections
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#default-attribute-values"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Default Attribute Values
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#configuring-eloquent-strictness"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Configuring Eloquent Strictness
                            </a>
                        </li>
                                    </ul>
                    </li>
            <li class="mt-1.5 py-0.5 first:mt-0">
            <a
                href="#retrieving-models"
                class="inline-block border-l-[3px] border-transparent pl-4 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
            >
                Retrieving Models
            </a>

                            <ul class="mt-1.5">
                                            <li class="py-0.5">
                            <a
                                href="#collections"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Collections
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#chunking-results"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Chunking Results
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#chunking-using-lazy-collections"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Chunk Using Lazy Collections
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#cursors"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Cursors
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#advanced-subqueries"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Advanced Subqueries
                            </a>
                        </li>
                                    </ul>
                    </li>
            <li class="mt-1.5 py-0.5 first:mt-0">
            <a
                href="#retrieving-single-models"
                class="inline-block border-l-[3px] border-transparent pl-4 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
            >
                Retrieving Single Models / Aggregates
            </a>

                            <ul class="mt-1.5">
                                            <li class="py-0.5">
                            <a
                                href="#retrieving-or-creating-models"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Retrieving or Creating Models
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#retrieving-aggregates"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Retrieving Aggregates
                            </a>
                        </li>
                                    </ul>
                    </li>
            <li class="mt-1.5 py-0.5 first:mt-0">
            <a
                href="#inserting-and-updating-models"
                class="inline-block border-l-[3px] border-transparent pl-4 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
            >
                Inserting and Updating Models
            </a>

                            <ul class="mt-1.5">
                                            <li class="py-0.5">
                            <a
                                href="#inserts"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Inserts
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#updates"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Updates
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#mass-assignment"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Mass Assignment
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#upserts"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Upserts
                            </a>
                        </li>
                                    </ul>
                    </li>
            <li class="mt-1.5 py-0.5 first:mt-0">
            <a
                href="#deleting-models"
                class="inline-block border-l-[3px] border-transparent pl-4 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
            >
                Deleting Models
            </a>

                            <ul class="mt-1.5">
                                            <li class="py-0.5">
                            <a
                                href="#soft-deleting"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Soft Deleting
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#querying-soft-deleted-models"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Querying Soft Deleted Models
                            </a>
                        </li>
                                    </ul>
                    </li>
            <li class="mt-1.5 py-0.5 first:mt-0">
            <a
                href="#pruning-models"
                class="inline-block border-l-[3px] border-transparent pl-4 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
            >
                Pruning Models
            </a>

                    </li>
            <li class="mt-1.5 py-0.5 first:mt-0">
            <a
                href="#replicating-models"
                class="inline-block border-l-[3px] border-transparent pl-4 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
            >
                Replicating Models
            </a>

                    </li>
            <li class="mt-1.5 py-0.5 first:mt-0">
            <a
                href="#query-scopes"
                class="inline-block border-l-[3px] border-transparent pl-4 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
            >
                Query Scopes
            </a>

                            <ul class="mt-1.5">
                                            <li class="py-0.5">
                            <a
                                href="#global-scopes"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Global Scopes
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#local-scopes"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Local Scopes
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#pending-attributes"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Pending Attributes
                            </a>
                        </li>
                                    </ul>
                    </li>
            <li class="mt-1.5 py-0.5 first:mt-0">
            <a
                href="#comparing-models"
                class="inline-block border-l-[3px] border-transparent pl-4 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
            >
                Comparing Models
            </a>

                    </li>
            <li class="mt-1.5 py-0.5 first:mt-0">
            <a
                href="#events"
                class="inline-block border-l-[3px] border-transparent pl-4 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
            >
                Events
            </a>

                            <ul class="mt-1.5">
                                            <li class="py-0.5">
                            <a
                                href="#events-using-closures"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Using Closures
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#observers"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Observers
                            </a>
                        </li>
                                            <li class="py-0.5">
                            <a
                                href="#muting-events"
                                class="inline-block border-l-[3px] border-transparent pl-8 text-[13px] text-sand-light-11 hover:border-sand-dark-4/25 hover:text-sand-light-12 dark:text-sand-dark-11 dark:hover:border-sand-light-4/25 dark:hover:text-sand-dark-12 [&[data-active='true']]:border-laravel-red [&[data-active='true']]:text-sand-light-12 [&[data-active='true']]:dark:text-sand-dark-12"
                            >
                                Muting Events
                            </a>
                        </li>
                                    </ul>
                    </li>
    </ul>
                            </div>
        
        <div class="mt-10 px-4">
            <div id="docs-ad"></div>

    <template id="promote-forge">
        <div
            class="docs-ad  aspect-200/275 w-full max-w-50"
        >
            <div class="relative h-full transition-transform hover:-translate-y-0.5">
                <a
                    href="https://forge.laravel.com"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="docs-ad-link relative flex h-full flex-col items-start justify-end gap-4 overflow-hidden rounded-lg bg-cover bg-center p-5 font-medium text-base/[120%]"
                    style="background-image: url('/images/ads/forge-ad-background.png')"
                >
                                            <img
                            src="/images/ads/forge-logo.svg"
                            class="h-4 w-auto"
                            alt="Laravel Forge"
                        />
                    
                                            <p class='tracking-[-0.3px] text-[#C6FFF5]'>Server management made simple for any PHP app</p>
                    
                    <div
                        class="inline-flex items-center gap-1.5 text-sm/[120%] text-white"
                    >
                        Learn more
                        <svg class="size-4 shrink-0" viewBox="0 0 16 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M12.001 10.5v-6h-6m-1.833 7.833 7.167-7.166"
                                stroke="currentColor"
                                stroke-width="1.5"
                                stroke-linecap="square"
                            />
                        </svg>
                    </div>
                </a>
                            </div>
        </div>
    </template>
    <template id="promote-cloud">
        <div
            class="docs-ad  aspect-200/275 w-full max-w-50"
        >
            <div class="relative h-full transition-transform hover:-translate-y-0.5">
                <a
                    href="https://cloud.laravel.com"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="docs-ad-link relative flex h-full flex-col items-start justify-end gap-4 overflow-hidden rounded-lg bg-cover bg-center p-5 font-medium text-base/[120%]"
                    style="background-image: url('/images/ads/cloud-ad-background.png')"
                >
                                            <img
                            src="/images/ads/cloud-logo.svg"
                            class="h-4 w-auto"
                            alt="Laravel Cloud"
                        />
                    
                                            <p class='tracking-[-0.3px] text-[#C1DBFF]'>The fastest way to deploy and scale Laravel apps</p>
                    
                    <div
                        class="inline-flex items-center gap-1.5 text-sm/[120%] text-white"
                    >
                        Learn more
                        <svg class="size-4 shrink-0" viewBox="0 0 16 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M12.001 10.5v-6h-6m-1.833 7.833 7.167-7.166"
                                stroke="currentColor"
                                stroke-width="1.5"
                                stroke-linecap="square"
                            />
                        </svg>
                    </div>
                </a>
                            </div>
        </div>
    </template>
    <template id="promote-nightwatch">
        <div
            class="docs-ad  aspect-200/275 w-full max-w-50"
        >
            <div class="relative h-full transition-transform hover:-translate-y-0.5">
                <a
                    href="https://nightwatch.laravel.com"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="docs-ad-link relative flex h-full flex-col items-start justify-end gap-4 overflow-hidden rounded-lg bg-cover bg-center p-5 font-medium text-base/[120%]"
                    style="background-image: url('/images/ads/nightwatch-ad-background.png')"
                >
                                            <img
                            src="/images/ads/nightwatch-logo.svg"
                            class="h-[18px] w-auto"
                            alt="Laravel Nightwatch"
                        />
                    
                                            <p class='tracking-[-0.3px] text-[#D3FFE7]'>First-class monitoring and deep insights for Laravel apps</p>
                    
                    <div
                        class="inline-flex items-center gap-1.5 text-sm/[120%] text-white"
                    >
                        Learn more
                        <svg class="size-4 shrink-0" viewBox="0 0 16 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M12.001 10.5v-6h-6m-1.833 7.833 7.167-7.166"
                                stroke="currentColor"
                                stroke-width="1.5"
                                stroke-linecap="square"
                            />
                        </svg>
                    </div>
                </a>
                            </div>
        </div>
    </template>
    <template id="promote-boost">
        <div
            class="docs-ad  aspect-200/275 w-full max-w-50"
        >
            <div class="relative h-full transition-transform hover:-translate-y-0.5">
                <a
                    href="https://laravel.com/ai/boost"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="docs-ad-link relative flex h-full flex-col items-start justify-end gap-4 overflow-hidden rounded-lg bg-cover bg-center p-5 font-medium text-base/[120%]"
                    style="background-image: url('/images/ads/boost-ad-background.png')"
                >
                                            <img
                            src="/images/ads/boost-logo.svg"
                            class="h-[18px] w-auto"
                            alt="Laravel Boost"
                        />
                    
                                            <p class='tracking-[-0.3px] text-[#FBE6FE]'>Supercharge your AI development with essential context</p>
                    
                    <div
                        class="inline-flex items-center gap-1.5 text-sm/[120%] text-white"
                    >
                        Learn more
                        <svg class="size-4 shrink-0" viewBox="0 0 16 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M12.001 10.5v-6h-6m-1.833 7.833 7.167-7.166"
                                stroke="currentColor"
                                stroke-width="1.5"
                                stroke-linecap="square"
                            />
                        </svg>
                    </div>
                </a>
                            </div>
        </div>
    </template>
    <template id="promote-laravel_live_japan">
        <div
            class="docs-ad  aspect-200/275 w-full max-w-50"
        >
            <div class="relative h-full transition-transform hover:-translate-y-0.5">
                <a
                    href="https://laravellive.jp"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="docs-ad-link relative flex h-full flex-col items-start justify-end gap-4 overflow-hidden rounded-lg bg-cover bg-center p-5 font-medium"
                    style="background-image: url('/images/ads/laravel-live-jp-ad-background.png')"
                >
                                            <img
                            src="/images/ads/laravel-live-jp-logo.svg"
                            class="h-5 w-auto"
                            alt="Laravel Live Japan"
                        />
                    
                                            <p class='font-mono tracking-[-0.3px] text-white uppercase'>May 26-27, 2026</span><br>Tokyo, Japan</span></p>
                    
                    <div
                        class="inline-flex items-center gap-1.5 text-sm/[120%] text-white font-mono tracking-[-.2px] uppercase"
                    >
                        Learn more
                        <svg class="size-4 shrink-0" viewBox="0 0 16 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M12.001 10.5v-6h-6m-1.833 7.833 7.167-7.166"
                                stroke="currentColor"
                                stroke-width="1.5"
                                stroke-linecap="square"
                            />
                        </svg>
                    </div>
                </a>
                            </div>
        </div>
    </template>

<script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script>
    async function getCountry() {
        try {
            const cached = localStorage.getItem('docs-ad-country');

            if (cached) {
                return cached;
            }

            const response = await fetch('/country');
            const { country } = await response.json();

            if (country) {
                localStorage.setItem('docs-ad-country', country);
            }

            return country;
        } catch (e) {
            return null;
        }
    }

    async function getAdKey(promotions) {
        const country = await getCountry();

        const eastAsia = [
            'JP',
            'KR',
            'CN',
            'TW',
            'HK',
            'MO',
            'MN',
            'TH',
            'VN',
            'PH',
            'MY',
            'SG',
            'ID',
            'MM',
            'KH',
            'LA',
            'BN',
        ];

        if (eastAsia.includes(country)) {
            return 'laravel_live_japan';
        }

        const keys = Object.keys(promotions);
        return keys[Math.floor(Math.random() * keys.length)];
    }

    (async function () {
        const docsAd = document.getElementById('docs-ad');
        const promotions = JSON.parse('{\u0022forge\u0022:{\u0022title\u0022:\u0022Laravel Forge\u0022,\u0022url\u0022:\u0022https:\\\/\\\/forge.laravel.com\u0022,\u0022background\u0022:\u0022forge-ad-background.png\u0022,\u0022logo\u0022:\u0022forge-logo.svg\u0022,\u0022logo_classes\u0022:\u0022h-4\u0022,\u0022text\u0022:\u0022\\u003Cp class=\\u0027tracking-[-0.3px] text-[#C6FFF5]\\u0027\\u003EServer management made simple for any PHP app\\u003C\\\/p\\u003E\u0022},\u0022cloud\u0022:{\u0022title\u0022:\u0022Laravel Cloud\u0022,\u0022url\u0022:\u0022https:\\\/\\\/cloud.laravel.com\u0022,\u0022background\u0022:\u0022cloud-ad-background.png\u0022,\u0022logo\u0022:\u0022cloud-logo.svg\u0022,\u0022logo_classes\u0022:\u0022h-4\u0022,\u0022text\u0022:\u0022\\u003Cp class=\\u0027tracking-[-0.3px] text-[#C1DBFF]\\u0027\\u003EThe fastest way to deploy and scale Laravel apps\\u003C\\\/p\\u003E\u0022},\u0022nightwatch\u0022:{\u0022title\u0022:\u0022Laravel Nightwatch\u0022,\u0022url\u0022:\u0022https:\\\/\\\/nightwatch.laravel.com\u0022,\u0022background\u0022:\u0022nightwatch-ad-background.png\u0022,\u0022logo\u0022:\u0022nightwatch-logo.svg\u0022,\u0022logo_classes\u0022:\u0022h-[18px]\u0022,\u0022text\u0022:\u0022\\u003Cp class=\\u0027tracking-[-0.3px] text-[#D3FFE7]\\u0027\\u003EFirst-class monitoring and deep insights for Laravel apps\\u003C\\\/p\\u003E\u0022},\u0022boost\u0022:{\u0022title\u0022:\u0022Laravel Boost\u0022,\u0022url\u0022:\u0022https:\\\/\\\/laravel.com\\\/ai\\\/boost\u0022,\u0022background\u0022:\u0022boost-ad-background.png\u0022,\u0022logo\u0022:\u0022boost-logo.svg\u0022,\u0022logo_classes\u0022:\u0022h-[18px]\u0022,\u0022text\u0022:\u0022\\u003Cp class=\\u0027tracking-[-0.3px] text-[#FBE6FE]\\u0027\\u003ESupercharge your AI development with essential context\\u003C\\\/p\\u003E\u0022},\u0022laravel_live_japan\u0022:{\u0022title\u0022:\u0022Laravel Live Japan\u0022,\u0022url\u0022:\u0022https:\\\/\\\/laravellive.jp\u0022,\u0022background\u0022:\u0022laravel-live-jp-ad-background.png\u0022,\u0022logo\u0022:\u0022laravel-live-jp-logo.svg\u0022,\u0022logo_classes\u0022:\u0022h-5\u0022,\u0022text\u0022:\u0022\\u003Cp class=\\u0027font-mono tracking-[-0.3px] text-white uppercase\\u0027\\u003EMay 26-27, 2026\\u003C\\\/span\\u003E\\u003Cbr\\u003ETokyo, Japan\\u003C\\\/span\\u003E\\u003C\\\/p\\u003E\u0022}}');
        const adKey = await getAdKey(promotions);
        const ad = promotions[adKey];
        const activePromotionTemplate = document.getElementById('promote-' + adKey);
        const activePromotionTitle = activePromotionTemplate.content.querySelector('img').getAttribute('alt');

        docsAd.appendChild(activePromotionTemplate.content);

        // check if ad should be hidden
        const adElement = docsAd.querySelector('.docs-ad');
        const closeButton = docsAd.querySelector('.docs-ad-close');
        const adLink = docsAd.querySelector('.docs-ad-link');

        // hide if previously closed
        try {
            if (localStorage.getItem('docs-ad-closed') === 'true' && false) {
                adElement.classList.add('xl:hidden');
                adElement.classList.remove('xl:block');
            }
        } catch (e) {
            // ignore localStorage errors
        }

        // handle the close button
        if (closeButton) {
            closeButton.addEventListener('click', function (e) {
                e.preventDefault();
                adElement.classList.add('xl:hidden');
                adElement.classList.remove('xl:block');

                try {
                    localStorage.setItem('docs-ad-closed', 'true');
                } catch (e) {
                    // ignore localStorage errors
                }

                // track close button click with rudderanalytics
                try {
                    if (typeof rudderanalytics !== 'undefined') {
                        rudderanalytics.track((ad.analytics_event || ad.title) + ' Ad Closed', {
                            category: 'User Actions',
                            label: (ad.analytics_label || ad.title) + ' Ad',
                            timestamp: new Date().toISOString(),
                        });
                    }
                } catch (e) {
                    // ignore rudderanalytics errors
                }
            });
        }

        // track ad clicks
        if (adLink) {
            adLink.addEventListener('click', function (e) {
                // prevent default link behavior
                e.preventDefault();

                // track ad click with rudderanalytics
                try {
                    if (typeof rudderanalytics !== 'undefined') {
                        rudderanalytics.track(
                            (ad.analytics_event || ad.title) + ' Ad Clicked',
                            {
                                category: 'User Actions',
                                label: (ad.analytics_label || ad.title) + ' Ad',
                                timestamp: new Date().toISOString(),
                            },
                            function () {
                                // navigate after tracking completes
                                window.open(adLink.href, '_blank', 'noopener,noreferrer');
                            },
                        );
                    } else {
                        // if rudderanalytics is not available, navigate immediately
                        window.open(adLink.href, '_blank', 'noopener,noreferrer');
                    }
                } catch (e) {
                    // if tracking fails, navigation still happens
                    window.open(adLink.href, '_blank', 'noopener,noreferrer');
                }
            });
        }
    })();
</script>
        </div>
    </div>
</div>
                    </div>
                </div>
</div>
        </div>
    </div>
            </div>
        </div>

        <div
    class="border-t border-neutral-200 bg-white dark:border-neutral-700 dark:bg-neutral-900"
>
    <div class="mx-auto w-full max-w-full px-4 pt-10 md:pt-24 xl:max-w-screen-xl xl:px-16">
        <div class="flex flex-col justify-between lg:flex-row lg:gap-12">
            <div class="w-full lg:w-1/4">
    <svg class="mb-6 h-10 w-10" width="42" height="42" viewBox="0 0 42 42" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path
        d="M41 9.88889L33 5.44444L25 9.88889M41 9.88889L33 14.3333M41 9.88889V18.7778L33 23.2222M25 9.88889V18.7778M25 9.88889L33 14.3333M25 18.7778L33 23.2222M25 18.7778L9 27.6667M33 23.2222V32.1111L17 41M33 23.2222V14.3333M33 23.2222L17 32.1111M9 27.6667L17 32.1111M9 27.6667V9.88889M1 5.44444L9 1L17 5.44444M1 5.44444V32.1111L17 41M1 5.44444L9 9.88889M17 41V32.1111M9 9.88889L17 5.44444M17 5.44444V23.2222"
        stroke="#F53003" stroke-width="1.5" />
</svg>    <p class="text-xl font-medium text-pretty text-laravel-red">
        Laravel is the most productive way to
        <br class="block lg:hidden" />
        build, deploy, and monitor software.
    </p>
    <ul class="my-8 flex items-center justify-start space-x-6 lg:my-16">
        <li>
            <a
                href="https://github.com/laravel"
                target="_blank"
                title="Laravel on GitHub"
                class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:hover:text-neutral-300"
            >
                <svg
    width="24"
    alt="GitHub icon"
    height="24"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
>
    <path
        fill-rule="evenodd"
        clip-rule="evenodd"
        d="M0 12.305C0 17.74 3.438 22.352 8.207 23.979C8.807 24.092 9.027 23.712 9.027 23.386C9.027 23.094 9.016 22.32 9.01 21.293C5.671 22.037 4.967 19.643 4.967 19.643C4.422 18.223 3.635 17.845 3.635 17.845C2.545 17.081 3.718 17.096 3.718 17.096C4.921 17.183 5.555 18.364 5.555 18.364C6.626 20.244 8.364 19.702 9.048 19.386C9.157 18.591 9.468 18.049 9.81 17.741C7.145 17.431 4.344 16.376 4.344 11.661C4.344 10.318 4.811 9.219 5.579 8.359C5.456 8.048 5.044 6.797 5.696 5.103C5.696 5.103 6.704 4.773 8.996 6.364C9.954 6.091 10.98 5.955 12.001 5.95C13.02 5.955 14.047 6.091 15.005 6.364C17.295 4.772 18.302 5.103 18.302 5.103C18.956 6.797 18.544 8.048 18.421 8.359C19.191 9.219 19.655 10.318 19.655 11.661C19.655 16.387 16.849 17.428 14.175 17.732C14.606 18.112 14.99 18.862 14.99 20.011C14.99 21.656 14.975 22.982 14.975 23.386C14.975 23.715 15.191 24.098 15.8 23.977C20.565 22.347 24 17.738 24 12.305C24 5.508 18.627 0 12 0C5.373 0 0 5.508 0 12.305Z"
        fill="currentColor"
    />
</svg>            </a>
        </li>
        <li>
            <a
                href="https://x.com/laravelphp"
                target="_blank"
                title="Laravel on X"
                class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:hover:text-neutral-300"
            >
                <svg
    width="24"
    height="24"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
>
    <path
        d="M13.969 10.1571L22.7069 0H20.6363L13.0491 8.81931L6.9893 0H0L9.16366 13.3364L0 23.9877H2.07073L10.083 14.6742L16.4826 23.9877H23.4719L13.9684 10.1571H13.969ZM11.1328 13.4538L10.2043 12.1258L2.81684 1.55881H5.99736L11.9592 10.0867L12.8876 11.4147L20.6373 22.4998H17.4567L11.1328 13.4544V13.4538Z"
        fill="currentColor"
    />
</svg>            </a>
        </li>
        <li>
            <a
                href="https://www.youtube.com/@LaravelPHP"
                target="_blank"
                title="Laravel on YouTube"
                class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:hover:text-neutral-300"
            >
                <svg
    width="35"
    height="24"
    viewBox="0 0 35 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
>
    <path
        d="M33.892 3.75519C33.4994 2.27706 32.3428 1.11294 30.8742 0.717875C28.2124 0 17.5385 0 17.5385 0C17.5385 0 6.8648 0 4.20286 0.717875C2.7343 1.113 1.57768 2.27706 1.18511 3.75519C0.471863 6.43437 0.471863 12.0243 0.471863 12.0243C0.471863 12.0243 0.471863 17.6141 1.18511 20.2933C1.57768 21.7714 2.7343 22.8871 4.20286 23.2821C6.8648 24 17.5385 24 17.5385 24C17.5385 24 28.2123 24 30.8742 23.2821C32.3428 22.8871 33.4994 21.7714 33.892 20.2933C34.6052 17.6141 34.6052 12.0243 34.6052 12.0243C34.6052 12.0243 34.6052 6.43437 33.892 3.75519ZM14.0476 17.0994V6.94906L22.9688 12.0244L14.0476 17.0994Z"
        fill="currentColor"
    />
</svg>            </a>
        </li>
        <li>
            <a
                href="https://discord.com/invite/laravel"
                target="_blank"
                title="Laravel on Discord"
                class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:hover:text-neutral-300"
            >
                <svg
    width="33"
    height="24"
    viewBox="0 0 33 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
>
    <path
        d="M27.4296 2.00996C25.3491 1.05745 23.1528 0.381713 20.8966 0C20.5879 0.551901 20.3086 1.11973 20.0598 1.70112C17.6566 1.33898 15.2127 1.33898 12.8095 1.70112C12.5605 1.11979 12.2812 0.551968 11.9726 0C9.71504 0.384937 7.51722 1.06228 5.43462 2.01494C1.30013 8.132 0.179328 14.0971 0.739727 19.9776C3.16099 21.7665 5.87108 23.127 8.75218 24C9.40092 23.1275 9.97497 22.2018 10.4682 21.2329C9.53134 20.883 8.62706 20.4512 7.76588 19.9427C7.99253 19.7783 8.2142 19.609 8.42839 19.4446C10.9342 20.623 13.6692 21.234 16.4384 21.234C19.2075 21.234 21.9425 20.623 24.4483 19.4446C24.665 19.6214 24.8867 19.7908 25.1108 19.9427C24.248 20.4521 23.3421 20.8846 22.4035 21.2354C22.8962 22.2039 23.4702 23.1287 24.1196 24C27.0031 23.1305 29.7153 21.7707 32.137 19.9801C32.7945 13.1606 31.0137 7.25031 27.4296 2.00996ZM11.1781 16.3611C9.61644 16.3611 8.32628 14.944 8.32628 13.2005C8.32628 11.457 9.57161 10.0274 11.1731 10.0274C12.7746 10.0274 14.0548 11.457 14.0274 13.2005C14 14.944 12.7696 16.3611 11.1781 16.3611ZM21.6986 16.3611C20.1345 16.3611 18.8493 14.944 18.8493 13.2005C18.8493 11.457 20.0946 10.0274 21.6986 10.0274C23.3026 10.0274 24.5729 11.457 24.5455 13.2005C24.5181 14.944 23.2902 16.3611 21.6986 16.3611Z"
        fill="currentColor"
    />
</svg>            </a>
        </li>
    </ul>

    <div>
        <ul class="flex justify-start space-x-8">
            <li class="text-neutral-500 dark:text-neutral-500">&copy; 2026 Laravel</li>
            <li>
                <a
                    href="https://laravel.com/legal"
                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                >
                    Legal
                </a>
            </li>
            <li>
                <a
                    href="https://status.laravel.com/"
                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                >
                    Status
                </a>
            </li>
        </ul>
    </div>
</div>
            <div class="grid w-full grid-cols-2 lg:flex lg:w-fit lg:flex-wrap lg:justify-end">
            <div class="mt-14 flex flex-wrap self-start lg:mt-0 lg:min-w-[164px] lg:flex-col">
            <h4 class="mb-8 w-full text-base font-medium text-neutral-900 lg:w-fit dark:text-neutral-100">
                Products
            </h4>

                                                <ul class="col-span-6 mb-6 space-y-6 lg:col-span-2 lg:mb-0">
                                                    <li>
                                <a
                                    href="https://cloud.laravel.com"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Cloud
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="https://forge.laravel.com"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Forge
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="https://nightwatch.laravel.com"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Nightwatch
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="https://vapor.laravel.com"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Vapor
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="https://nova.laravel.com"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Nova
                                </a>
                            </li>
                                            </ul>
                                    </div>
            <div class="mt-14 flex flex-wrap self-start lg:mt-0 lg:min-w-[164px] lg:flex-col">
            <h4 class="mb-8 w-full text-base font-medium text-neutral-900 lg:w-fit dark:text-neutral-100">
                Packages
            </h4>

                                                <ul class="col-span-6 mb-6 space-y-6 lg:col-span-2 lg:mb-0">
                                                    <li>
                                <a
                                    href="/docs/cashier"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Cashier
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/docs/dusk"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Dusk
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/docs/horizon"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Horizon
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/docs/octane"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Octane
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/docs/scout"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Scout
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/docs/pennant"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Pennant
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/docs/pint"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Pint
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/docs/sail"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Sail
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/docs/sanctum"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Sanctum
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/docs/socialite"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Socialite
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/docs/telescope"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Telescope
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/docs/pulse"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Pulse
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/docs/reverb"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Reverb
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/docs/broadcasting"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Echo
                                </a>
                            </li>
                                            </ul>
                                    </div>
            <div class="mt-14 flex flex-wrap self-start lg:mt-0 lg:min-w-[164px] lg:flex-col">
            <h4 class="mb-8 w-full text-base font-medium text-neutral-900 lg:w-fit dark:text-neutral-100">
                Resources
            </h4>

                                                <ul class="col-span-6 mb-6 space-y-6 lg:col-span-2 lg:mb-0">
                                                    <li>
                                <a
                                    href="/docs"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Documentation
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/starter-kits"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Starter Kits
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/docs/releases"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Release Notes
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/blog"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Blog
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="https://laravel-news.com"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    News
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/community"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Community
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="https://larabelles.com/"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Larabelles
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/learn"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Learn
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="https://larajobs.com/?partner=5"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Jobs
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="/careers"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Careers
                                </a>
                            </li>
                                                    <li>
                                <a
                                    href="https://trust.laravel.com"
                                    referrerpolicy="no-referrer-when-downgrade"
                                    class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                >
                                    Trust
                                </a>
                            </li>
                                            </ul>
                                    </div>
            <div class="mt-14 flex flex-wrap self-start lg:mt-0 lg:min-w-[164px] lg:flex-col">
            <h4 class="mb-8 w-full text-base font-medium text-neutral-900 lg:w-fit dark:text-neutral-100">
                Partners
            </h4>

                            
                <ul
                    x-data="{
                        partners: JSON.parse('[[\u0022Bacancy\u0022,\u0022https:\\\/\\\/partners.laravel.com\\\/partners\\\/bacancy\u0022],[\u0022Tighten\u0022,\u0022https:\\\/\\\/partners.laravel.com\\\/partners\\\/tighten\u0022],[\u0022CACI\u0022,\u0022https:\\\/\\\/partners.laravel.com\\\/partners\\\/caci-limited\u0022],[\u0022byte5\u0022,\u0022https:\\\/\\\/partners.laravel.com\\\/partners\\\/byte5\u0022],[\u0022UCodeSoft\u0022,\u0022https:\\\/\\\/partners.laravel.com\\\/partners\\\/ucodesoft\u0022],[\u002264 Robots\u0022,\u0022https:\\\/\\\/partners.laravel.com\\\/partners\\\/64-robots\u0022],[\u0022Steadfast Collective\u0022,\u0022https:\\\/\\\/partners.laravel.com\\\/partners\\\/steadfast-collective\u0022],[\u0022Threadable\u0022,\u0022https:\\\/\\\/partners.laravel.com\\\/partners\\\/threadable\u0022],[\u0022Jump24\u0022,\u0022https:\\\/\\\/partners.laravel.com\\\/partners\\\/jump24\u0022],[\u0022Kirschbaum\u0022,\u0022https:\\\/\\\/partners.laravel.com\\\/partners\\\/kirschbaum\u0022],[\u0022Swoo\u0022,\u0022https:\\\/\\\/partners.laravel.com\\\/partners\\\/swoo\u0022],[\u0022Curotec\u0022,\u0022https:\\\/\\\/partners.laravel.com\\\/partners\\\/curotec\u0022],[\u0022Redberry\u0022,\u0022https:\\\/\\\/partners.laravel.com\\\/partners\\\/redberry\u0022],[\u0022Vehikl\u0022,\u0022https:\\\/\\\/partners.laravel.com\\\/partners\\\/vehikl\u0022]]'),
                        shuffled: [],
                        init() {
                            this.shuffled = [...this.partners].sort(() => Math.random() - 0.5)
                        },
                    }"
                    class="col-span-6 mb-6 space-y-6 lg:col-span-2 lg:mb-0"
                >
                    <template x-for="partner in shuffled" :key="partner[1]">
                        <li>
                            <a
                                :href="partner[1]"
                                class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                                x-text="partner[0]"
                            ></a>
                        </li>
                    </template>
                    <li>
                        <a
                            href="https://partners.laravel.com"
                            class="text-neutral-500 transition duration-100 hover:text-neutral-700 dark:text-neutral-500 dark:hover:text-neutral-300"
                        >
                            More Partners
                        </a>
                    </li>
                </ul>
                    </div>
    </div>
        </div>
        <div class="mt-24 w-full text-neutral-100">
            <svg class="h-full w-full text-laravel-red"
    width="1280"
    height="308"
    viewBox="0 0 1280 308"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
>
    <path
        d="M50.2753 0H0V308.689H144.713V263.27H50.2753V0Z"
        fill="currentColor"
    />
    <path
        d="M322.209 130.973C315.796 120.684 306.688 112.602 294.883 106.718C283.081 100.84 271.201 97.8969 259.253 97.8969C243.798 97.8969 229.665 100.764 216.843 106.496C204.014 112.228 193.015 120.099 183.834 130.091C174.654 140.088 167.51 151.628 162.412 164.706C157.308 177.792 154.761 191.54 154.761 205.94C154.761 220.645 157.308 234.457 162.412 247.39C167.508 260.332 174.652 271.796 183.834 281.788C193.015 291.785 204.017 299.647 216.843 305.379C229.665 311.111 243.798 313.978 259.253 313.978C271.201 313.978 283.081 311.038 294.883 305.159C306.688 299.282 315.796 291.197 322.209 280.904V308.685H369.865V103.186H322.209V130.973ZM317.837 231.076C314.922 239.016 310.841 245.925 305.598 251.804C300.35 257.687 294.009 262.389 286.579 265.917C279.146 269.445 270.905 271.208 261.875 271.208C252.837 271.208 244.676 269.445 237.391 265.917C230.104 262.389 223.839 257.687 218.593 251.804C213.345 245.925 209.335 239.016 206.57 231.076C203.794 223.138 202.417 214.759 202.417 205.942C202.417 197.12 203.794 188.742 206.57 180.804C209.335 172.866 213.345 165.961 218.593 160.078C223.839 154.201 230.102 149.493 237.391 145.965C244.676 142.437 252.837 140.674 261.875 140.674C270.908 140.674 279.146 142.437 286.579 145.965C294.009 149.493 300.35 154.199 305.598 160.078C310.844 165.961 314.922 172.866 317.837 180.804C320.748 188.742 322.209 197.12 322.209 205.942C322.209 214.759 320.748 223.138 317.837 231.076Z"
        fill="currentColor"
    />
    <path
        d="M709.568 130.973C703.155 120.684 694.047 112.602 682.242 106.718C670.44 100.84 658.56 97.8969 646.612 97.8969C631.157 97.8969 617.024 100.764 604.202 106.496C591.373 112.228 580.374 120.099 571.193 130.091C562.013 140.088 554.869 151.628 549.771 164.706C544.666 177.792 542.12 191.54 542.12 205.94C542.12 220.645 544.666 234.457 549.771 247.39C554.867 260.332 562.01 271.796 571.193 281.788C580.374 291.785 591.375 299.647 604.202 305.379C617.024 311.111 631.157 313.978 646.612 313.978C658.56 313.978 670.44 311.038 682.242 305.159C694.047 299.282 703.155 291.197 709.568 280.904V308.685H757.224V103.186H709.568V130.973ZM705.198 231.076C702.283 239.016 698.202 245.925 692.959 251.804C687.711 257.687 681.37 262.389 673.94 265.917C666.507 269.445 658.266 271.208 649.236 271.208C640.198 271.208 632.037 269.445 624.752 265.917C617.465 262.389 611.2 257.687 605.954 251.804C600.706 245.925 596.696 239.016 593.931 231.076C591.155 223.138 589.778 214.759 589.778 205.942C589.778 197.12 591.155 188.742 593.931 180.804C596.696 172.866 600.706 165.961 605.954 160.078C611.2 154.201 617.463 149.493 624.752 145.965C632.037 142.437 640.198 140.674 649.236 140.674C658.269 140.674 666.507 142.437 673.94 145.965C681.37 149.493 687.711 154.199 692.959 160.078C698.205 165.961 702.283 172.866 705.198 180.804C708.109 188.742 709.57 197.12 709.57 205.942C709.568 214.759 708.107 223.138 705.198 231.076Z"
        fill="currentColor"
    />
    <path
        d="M1280 1.12315e-05H1232.35V308.689H1280V1.12315e-05Z"
        fill="currentColor"
    />
    <path
        d="M407.466 308.689H455.117V150.486H536.876V103.192H407.466V308.689Z"
        fill="currentColor"
    />
    <path
        d="M948.281 103.192L888.386 260.557L828.489 103.192H780.224L858.441 308.689H918.331L996.546 103.192H948.281Z"
        fill="currentColor"
    />
    <path
        d="M1100.48 97.908C1042.13 97.908 995.937 146.279 995.937 205.944C995.937 271.9 1040.64 313.98 1106.59 313.98C1143.5 313.98 1167.06 299.745 1195.85 268.746L1163.66 243.621C1163.64 243.646 1139.36 275.802 1103.1 275.802C1060.96 275.802 1043.22 241.533 1043.22 223.803H1201.32C1209.62 155.913 1165.37 97.908 1100.48 97.908ZM1043.35 188.085C1043.71 184.13 1049.2 136.086 1100.1 136.086C1151.01 136.086 1157.19 184.123 1157.55 188.085H1043.35Z"
        fill="currentColor"
    />
</svg>    </div>
    </div>
</div>

        <script type="text/javascript">
            !(function () {
                'use strict';
                window.RudderSnippetVersion = '3.0.60';
                var e = 'rudderanalytics';
                window[e] || (window[e] = []);
                var rudderanalytics = window[e];
                if (Array.isArray(rudderanalytics)) {
                    if (true === rudderanalytics.snippetExecuted && window.console && console.error) {
                        console.error('RudderStack JavaScript SDK snippet included more than once.');
                    } else {
                        ((rudderanalytics.snippetExecuted = true), (window.rudderAnalyticsBuildType = 'legacy'));
                        var sdkBaseUrl = 'https://cdn.rudderlabs.com';
                        var sdkVersion = 'v3';
                        var sdkFileName = 'rsa.min.js';
                        var scriptLoadingMode = 'async';
                        var r = [
                            'setDefaultInstanceKey',
                            'load',
                            'ready',
                            'page',
                            'track',
                            'identify',
                            'alias',
                            'group',
                            'reset',
                            'setAnonymousId',
                            'startSession',
                            'endSession',
                            'consent',
                        ];
                        for (var n = 0; n < r.length; n++) {
                            var t = r[n];
                            rudderanalytics[t] = (function (r) {
                                return function () {
                                    var n;
                                    Array.isArray(window[e])
                                        ? rudderanalytics.push([r].concat(Array.prototype.slice.call(arguments)))
                                        : null === (n = window[e][r]) || void 0 === n || n.apply(window[e], arguments);
                                };
                            })(t);
                        }
                        try {
                            (new Function(
                                'class Test{field=()=>{};test({prop=[]}={}){return prop?(prop?.property??[...prop]):import("");}}',
                            ),
                                (window.rudderAnalyticsBuildType = 'modern'));
                        } catch (i) {}
                        var d = document.head || document.getElementsByTagName('head')[0];
                        var o = document.body || document.getElementsByTagName('body')[0];
                        ((window.rudderAnalyticsAddScript = function (e, r, n) {
                            var t = document.createElement('script');
                            ((t.src = e),
                                t.setAttribute('data-loader', 'RS_JS_SDK'),
                                r && n && t.setAttribute(r, n),
                                'async' === scriptLoadingMode
                                    ? (t.async = true)
                                    : 'defer' === scriptLoadingMode && (t.defer = true),
                                d ? d.insertBefore(t, d.firstChild) : o.insertBefore(t, o.firstChild));
                        }),
                            (window.rudderAnalyticsMount = function () {
                                (!(function () {
                                    if ('undefined' == typeof globalThis) {
                                        var e;
                                        var r = (function getGlobal() {
                                            return 'undefined' != typeof self
                                                ? self
                                                : 'undefined' != typeof window
                                                  ? window
                                                  : null;
                                        })();
                                        r &&
                                            Object.defineProperty(r, 'globalThis', {
                                                value: r,
                                                configurable: true,
                                            });
                                    }
                                })(),
                                    window.rudderAnalyticsAddScript(
                                        ''
                                            .concat(sdkBaseUrl, '/')
                                            .concat(sdkVersion, '/')
                                            .concat(window.rudderAnalyticsBuildType, '/')
                                            .concat(sdkFileName),
                                        'data-rsa-write-key',
                                        '2w8mFiDWValXyby6yHwgkH3Pb8X',
                                    ));
                            }),
                            'undefined' == typeof Promise || 'undefined' == typeof globalThis
                                ? window.rudderAnalyticsAddScript(
                                      'https://polyfill-fastly.io/v3/polyfill.min.js?version=3.111.0&features=Symbol%2CPromise&callback=rudderAnalyticsMount',
                                  )
                                : window.rudderAnalyticsMount());
                        var loadOptions = {};
                        rudderanalytics.load(
                            '2w8mFiDWValXyby6yHwgkH3Pb8X',
                            'https://laraveltrxdkoq.dataplane.rudderstack.com',
                            loadOptions,
                        );
                    }
                }
            })();
        </script>
        <script>
            if (typeof rudderanalytics !== 'undefined') {
                rudderanalytics.page();
            }
        </script>

        
            <script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'9dadc3997c5f91f0-SJC',t:'MTc3MzI2NTcxNA=='};var a=document.createElement('script');a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>
</html>
