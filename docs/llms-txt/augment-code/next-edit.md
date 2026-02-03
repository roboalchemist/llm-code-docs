# Source: https://docs.augmentcode.com/using-augment/next-edit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Next Edit

> Use Next Edit to flow through complex changes across your codebase. Cut down the time you spend on repetitive work like refactors, library upgrades, and schema changes.


export const NextEditSettingsIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg width="16" height="16" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="currentColor">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M19.85 8.75l4.15.83v4.84l-4.15.83 2.35 3.52-3.43 3.43-3.52-2.35-.83 4.15H9.58l-.83-4.15-3.52 2.35-3.43-3.43 2.35-3.52L0 14.42V9.58l4.15-.83L1.8 5.23 5.23 1.8l3.52 2.35L9.58 0h4.84l.83 4.15 3.52-2.35 3.43 3.43-2.35 3.52zm-1.57 5.07l4-.81v-2l-4-.81-.54-1.3 2.29-3.43-1.43-1.43-3.43 2.29-1.3-.54-.81-4h-2l-.81 4-1.3.54-3.43-2.29-1.43 1.43L6.38 8.9l-.54 1.3-4 .81v2l4 .81.54 1.3-2.29 3.43 1.43 1.43 3.43-2.29 1.3.54.81 4h2l.81-4 1.3-.54 3.43 2.29 1.43-1.43-2.29-3.43.54-1.3zm-8.186-4.672A3.43 3.43 0 0 1 12 8.57 3.44 3.44 0 0 1 15.43 12a3.43 3.43 0 1 1-5.336-2.852zm.956 4.274c.281.188.612.288.95.288A1.7 1.7 0 0 0 13.71 12a1.71 1.71 0 1 0-2.66 1.422z" />
    </svg>
  </div>;

export const NextEditDiffIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M10.7099 1.28902L13.7099 4.28902L13.9999 4.99902V13.999L12.9999 14.999H3.99994L2.99994 13.999V1.99902L3.99994 0.999023H9.99994L10.7099 1.28902ZM3.99994 13.999H12.9999V4.99902L9.99994 1.99902H3.99994V13.999ZM8 5.99902H6V6.99902H8V8.99902H9V6.99902H11V5.99902H9V3.99902H8V5.99902ZM6 10.999H11V11.999H6V10.999Z" />
    </svg>
  </div>;

export const NextEditPencil = () => <div className="inline-block w-4 h-4 mr-2">
    <svg width="16px" height="16px" viewBox="0 0 16 16" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <title>nextedit_available_dark</title>
    <g id="nextedit_available_dark" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <path d="M11.0070258,7 C11.1334895,7 11.2318501,6.90866511 11.2529274,6.76814988 C11.5409836,4.95550351 11.8641686,4.52693208 13.7751756,4.2529274 C13.9156909,4.23185012 14,4.13348946 14,4 C14,3.8735363 13.9156909,3.77517564 13.7751756,3.75409836 C11.8571429,3.48009368 11.618267,3.07259953 11.2529274,1.21779859 C11.2248244,1.09133489 11.1334895,1 11.0070258,1 C10.8735363,1 10.7751756,1.09133489 10.7540984,1.22482436 C10.4660422,3.07259953 10.1498829,3.48009368 8.23887588,3.75409836 C8.09836066,3.78220141 8.00702576,3.8735363 8.00702576,4 C8.00702576,4.13348946 8.09836066,4.23185012 8.23887588,4.2529274 C10.1569087,4.52693208 10.4028103,4.92740047 10.7540984,6.77517564 C10.7822014,6.91569087 10.8805621,7 11.0070258,7 Z" id="Path" fill="#BF5AF2"></path>
        <path d="M14.0056206,8.8 C14.0814988,8.8 14.1405152,8.74519906 14.1531616,8.66088993 C14.3259953,7.57330211 14.5199063,7.31615925 15.6665105,7.15175644 C15.7508197,7.13911007 15.8014052,7.08009368 15.8014052,7 C15.8014052,6.92412178 15.7508197,6.86510539 15.6665105,6.85245902 C14.5156909,6.68805621 14.3723653,6.44355972 14.1531616,5.33067916 C14.1362998,5.25480094 14.0814988,5.2 14.0056206,5.2 C13.9255269,5.2 13.8665105,5.25480094 13.8538642,5.33489461 C13.6810304,6.44355972 13.4913349,6.68805621 12.3447307,6.85245902 C12.2604215,6.86932084 12.2056206,6.92412178 12.2056206,7 C12.2056206,7.08009368 12.2604215,7.13911007 12.3447307,7.15175644 C13.4955504,7.31615925 13.6430913,7.55644028 13.8538642,8.66510539 C13.870726,8.74941452 13.9297424,8.8 14.0056206,8.8 Z" id="Path-Copy" fill="#BF5AF2" opacity="0.600000024"></path>
        <g id="Pencil_Base" fill="#168AFF">
            <path d="M3.07557525,3.27946831 C3.10738379,3.27258798 3.13664209,3.26682472 3.16597818,3.26160513 C3.19407786,3.25661079 3.22181021,3.25217747 3.24959807,3.24822758 C3.3431507,3.23490837 3.43787348,3.22705558 3.53270619,3.22474499 C3.54619312,3.22441336 3.56021661,3.22418981 3.57424082,3.22408741 L3.59202055,3.22402251 C3.61600759,3.22402251 3.63999463,3.22437692 3.66397314,3.22508575 C3.69176119,3.22590043 3.72012236,3.22722855 3.74845755,3.22905289 C3.77692744,3.23089046 3.80498198,3.23319023 3.83299719,3.23597733 C3.86236278,3.23889105 3.89230728,3.24242516 3.92218997,3.24651769 C3.95842477,3.25149198 3.99379267,3.25714552 4.02904516,3.2635852 C4.04457753,3.26641925 4.06056799,3.26950351 4.07653203,3.27274998 C4.1217801,3.28195855 4.16647313,3.29238022 4.21089814,3.30408537 C4.22093231,3.3067264 4.23153789,3.30959531 4.24212737,3.31253756 C4.27196202,3.32083528 4.30106886,3.32952376 4.33003598,3.33877116 C4.35855924,3.347869 4.38751122,3.35771229 4.41630528,3.3681193 C4.42116985,3.36987869 4.42551008,3.37146263 4.42984665,3.3730594 C4.4761162,3.39008583 4.52241276,3.4087674 4.56821184,3.42893807 C4.59406406,3.44033198 4.61917606,3.45191971 4.64412424,3.46396063 C4.67111495,3.47697976 4.69839649,3.4907848 4.72546291,3.50513959 C4.75890801,3.52288219 4.79178851,3.54132453 4.82431475,3.56059431 C4.8374698,3.56838641 4.85073285,3.5764165 4.86393439,3.58458539 C4.89491851,3.60376145 4.92539479,3.6235868 4.95550936,3.64416832 C4.9772823,3.65904443 4.99913454,3.67451232 5.02078256,3.69038541 C5.03998798,3.70447076 5.05881967,3.71870909 5.07748715,3.73325923 C5.10440445,3.75423289 5.13126725,3.7760983 5.15775949,3.79862613 C5.1821715,3.81939236 5.20595148,3.84042939 5.22940861,3.86201411 C5.24512436,3.87647694 5.26059993,3.89109333 5.27592752,3.90595256 C5.28442786,3.91418351 5.29385225,3.92345739 5.30321896,3.9328241 L10.2031018,8.83270693 C10.255475,8.88508012 10.3065885,8.93859789 10.3564099,8.99321224 L10.2031018,8.83270693 C10.2748395,8.90444467 10.344214,8.97832987 10.4111413,9.05423915 C10.4223877,9.06699478 10.4335715,9.07981507 10.4446856,9.092692 C10.7663645,9.46539004 11.0297601,9.88553066 11.2252237,10.3388957 L11.6780206,11.3880225 L12.548286,13.4076516 C12.7467158,13.8678966 12.5344727,14.4018581 12.0742277,14.6002879 C11.9977866,14.6332447 11.9179446,14.6552159 11.836969,14.6662015 L11.7149387,14.6744406 C11.592625,14.6744406 11.4703113,14.6497231 11.3556497,14.6002879 L11.2340206,14.5480225 L9.33602055,13.7300225 L8.28689372,13.2772256 C7.83352871,13.081762 7.41338809,12.8183665 7.04069004,12.4966876 L7.0022372,12.4631433 C6.98177889,12.4451057 6.9614676,12.4268903 6.94130575,12.4084989 L7.04069004,12.4966876 C6.95122931,12.4194733 6.86450207,12.3389008 6.78070498,12.2551038 L1.88082214,7.35522092 C0.935753358,6.41015213 0.935753358,4.87789288 1.88082214,3.9328241 L1.90902055,3.90502251 L2.01192506,3.8109306 C2.19120357,3.65606766 2.38780913,3.5318516 2.59488381,3.4382824 C2.62872186,3.42311621 2.65522016,3.41182111 2.68187195,3.40102033 C2.76025666,3.36925866 2.83986347,3.34180278 2.92043821,3.31861145 L3.07557525,3.27946831 Z M9.58610551,9.95149698 L7.89951995,11.6381324 C8.10279642,11.805046 8.32371441,11.9494547 8.55841217,12.068738 L8.76594574,12.166096 L10.2570206,12.8090225 L10.7570206,12.3090225 L10.114094,10.8179477 C9.97930356,10.5053101 9.80144069,10.2137385 9.58610551,9.95149698 Z" id="Combined-Shape" fill-rule="nonzero"></path>
            <rect id="Rectangle" opacity="0.005" x="0" y="0" width="16" height="16" rx="2"></rect>
        </g>
    </g>
    </svg>
  </div>;

export const Availability = ({tags = []}) => {
  const tagColor = {
    invite: "purple",
    beta: "gray",
    "private-preview": "purple",
    vscode: "blue",
    jetbrains: "orange",
    vim: "gray",
    neovim: "gray",
    cli: "green"
  };
  return <div className="flex items-center space-x-2 border-b pb-4 border-gray-200 dark:border-white/10">
      <span className="text-sm font-medium">Availability</span>
      {tags.map(tag => <Badge key={tag} size="sm" color={tagColor[tag] || "gray"}>
          {tag}
        </Badge>)}
    </div>;
};

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

<Availability tags={["vscode"]} />

## About Next Edit

<iframe class="w-full aspect-video rounded-md" src="https://www.youtube.com/embed/GPQgQpXbunc?si=opEGaxWlnWWtDimK" title="Feature Intro: Augment Next Edit" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

Next Edit helps you complete your train of thought by suggesting changes based on
your recent work and other context. You can jump to the next edit and quickly accept or
reject the suggested change with a single keystroke.

## Using Next Edit

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-example.webp?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=15d2c45a86087dbf50527e6fd6f2fcbf" className="rounded-xl" data-og-width="800" width="800" data-og-height="269" height="269" data-path="images/next-edit-example.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-example.webp?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f5012d087f9b3d75b1ffbe6f3e9377b9 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-example.webp?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=bc7568485ba1b35dc4a8e2328d44be52 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-example.webp?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=9efd8d51d0a8454f4dcc67b1bcc7e6f1 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-example.webp?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=133205b0f221da141c170291e6a712c7 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-example.webp?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b1a1323ffd4c70f32c314563c3415865 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-example.webp?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7991b04dd64d5e34638c3ec2e055f638 2500w" />

When Next Edit has a suggestion available, you will see a gutter icon and a summary
of the change in gray at the end of the line.
To jump to the next suggestion, press <Keyboard shortcut="Cmd/Ctrl ;" /> and
after reviewing the change, press <Keyboard shortcut="Enter" /> to accept
or <Keyboard shortcut="Backspace" /> to reject. If there are multiple
changes, press <Keyboard shortcut="Cmd/Ctrl ;" /> to accept and go to the
next suggestion.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-before.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2da1f3c529ce412004a7ed76ed9f7f6b" className="rounded-xl" data-og-width="1462" width="1462" data-og-height="447" height="447" data-path="images/next-edit-before.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-before.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=0eb68374ca0a2c27fdad7a7b03f83607 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-before.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a8814149922d202be7f35bcdca312c51 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-before.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=45a4363821b32aecef32a97c0eb61afd 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-before.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=1f9b79e4de971adac4dada7b8d82d796 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-before.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e8aec093ceccb9149bcd11a4093fdc24 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-before.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d77a87e90ab11569419ab6ddfd62952f 2500w" />

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-after.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4a4da9a295d213befb4787f8f32db0c3" className="rounded-xl" data-og-width="1462" width="1462" data-og-height="447" height="447" data-path="images/next-edit-after.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-after.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e4cc486dd570c612801d2cf45a8b5c2d 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-after.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4225a043bd285ccb80727b2414049819 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-after.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d515db036c6c0a2e74542fbab2b01e40 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-after.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2fee9ca15c32226d7122c870d2cee767 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-after.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=83ad3d37fa57e5c619b2b7c4e51bfdbf 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-after.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=dd22baa4f4973628ef4b6c310a225de2 2500w" />

By default, Next Edit will briefly highlight which parts of the existing code will
change before applying the change and highlighting the new code. Use Undo
(<Keyboard shortcut="Cmd/Ctrl Z" />) and Redo
(<Keyboard shortcut="Cmd Shift Z/Ctrl Y" />) to manually review the change.
You can configure this behavior in your Augment extension settings.

### Keyboard Shortcuts

<Tabs>
  <Tab title="MacOS">
    | Action            | Default shortcut                    |
    | :---------------- | :---------------------------------- |
    | Go to next        | <Keyboard shortcut="Cmd ;" />       |
    | Go to previous    | <Keyboard shortcut="Cmd Shift ;" /> |
    | Accept suggestion | <Keyboard shortcut="Enter" />       |
    | Reject suggestion | <Keyboard shortcut="Backspace" />   |
  </Tab>

  <Tab title="Windows/Linux">
    | Action            | Default shortcut                     |
    | :---------------- | :----------------------------------- |
    | Go to next        | <Keyboard shortcut="Ctrl ;" />       |
    | Go to previous    | <Keyboard shortcut="Ctrl Shift ;" /> |
    | Accept suggestion | <Keyboard shortcut="Enter" />        |
    | Reject suggestion | <Keyboard shortcut="Backspace" />    |
  </Tab>
</Tabs>

### Next Edit Indicators And Actions

There are several indicators to let you know Next Edits are available:

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-1.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d430e246380007353fb051329d5fe5c0" className="rounded-xl" data-og-width="1321" width="1321" data-og-height="493" height="493" data-path="images/next-edit-indicators-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-1.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7891da274cf6c865d15111e74b6ef820 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-1.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=91ce4241983c21e7292035b0200e3c2f 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-1.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c60a652018795ef075189345dd70a6df 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-1.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4571970e9457d34f15a446aba7cc2d94 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-1.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=53c7de6e5e691db931866dd603d61a03 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-1.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b9f5440a70f7dc5d40a3bd4fc403f8da 2500w" />

1. **Editor Title Icon** (Top Right): Changes colors when next edits are available.
   Click on the <NextEditPencil /> icon to open the next edit menu for
   additional actions like enabling/disabling the feature or accessing settings.
2. **Gutter Icon** (Left) - Indicates which lines will be changed by the suggestion
   and whether it will insert, delete or change code.
3. **Grey Text** (Right) -  appears on the line with the suggestion on screen with a
   brief summary of the change and the keybinding to press (typically
   <Keyboard shortcut="Cmd/Ctrl ;" />).

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-2.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=461d6b6607c9676e5ec7e691bd1d466d" className="rounded-xl" data-og-width="1322" width="1322" data-og-height="136" height="136" data-path="images/next-edit-indicators-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-2.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=fab3666721b4f18842ee57ae232c7c98 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-2.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=543b6460fdb6a499ed1b4a3914a787a8 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-2.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c201443209c6b06bd5f2e9e61e21b3dd 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-2.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=3bd7d2ecacc875128a22079b5dffad2d 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-2.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=52ade466db783f9248a3c3650e482892 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/next-edit-indicators-2.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c949c4bc61b0570c0495ff9fffc0e58e 2500w" />

4. **Hint Box** (Bottom Left) - appears when the next suggestion is off screen with
   brief summary of the change and the keybinding to press (typically
   <Keyboard shortcut="Cmd/Ctrl ;" />).

The tooltip also presents a few actions as icons:

* <NextEditDiffIcon /> Toggles showing diffs for suggestions in the tooltip.
* <NextEditSettingsIcon /> Opens Next Edit settings.

### Next Edit Settings

You can configure Next Edit settings in your Augment extension settings.
To open Augment extension settings, either navigate to the option through the pencil
menu, or open the Augment Commands panel by pressing
<Keyboard shortcut="Cmd/Ctrl Shift A" /> and select <Command text="⚙ Edit Settings" />.

Here are some notable settings:

* <Command text="Augment > Next Edit: Enable Background Suggestions" />: Use to enable or
  disable the feature.
* <Command text="Augment > Next Edit: Enable Global Background Suggestions" />: When enabled, Next
  Edits will suggest changes in other files via the hint box.
* <Command text="Augment > Next Edit: Enable Auto Apply" />: When enabled, Next
  Edits will automatically apply changes when you jump to them.
* <Command text="Augment > Next Edit: Show Diff in Hover" />: When enabled,
  Next Edits will show a diff of the suggested change in the hover.
* <Command text="Augment > Next Edit: Highlight Suggestions in The Editor" />: When enabled,
  Next Edits will highlight all lines with a suggestion in addition to showing gutter
  icons and grey text.
