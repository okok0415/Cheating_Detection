import React from 'react';
import * as AiIcons from "react-icons/ai";
import * as BsIcons from "react-icons/bs";
import * as FiIcons from "react-icons/fi";

export const SidebarData = [
    {
        title: 'Home',
        path: '/',
        icon: <AiIcons.AiFillHome />,
        cName: 'nav-text'
    },
    {
        title: 'Login',
        path: '/Login',
        icon: <FiIcons.FiLogIn />,
        cName: 'nav-text'
    },
    {
        title: 'Board',
        path: '/Board',
        icon: <BsIcons.BsClipboard />,
        cName: 'nav-text'
    },
    {
        title: 'ScreenSharing',
        path: '/ScreenSharing',
        icon: <FiIcons.FiMonitor />,
        cName: 'nav-text'
    },
]