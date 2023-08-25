import React, { Component } from 'react';
import { VideoCameraIcon } from '@heroicons/react/24/outline';
import { Link } from 'react-router-dom';


class LeaderboardHub extends Component {	
    render() {
        return (
            <div className='bg-gradient-to-b from-amber-100 via-amber-100 to-white'>
                <div className='container px-5 mx-auto text-center lg:px-40'>
                    <div className='flex flex-col w-full mb-10'>
                        <VideoCameraIcon className='mx-auto inline-block w-10 py-10' />
                        <h1 className='sm:text-4xl text-3xl font-medium title-font font-display'>
                            Spectating
                        </h1>
                        
                    </div>

                    <h1 className='text-2xl font-medium mb-10'>Select the game</h1>

                    {/*Buttons*/}
                    <div className='inline-flex gap-x-4 pb-4'>
                        <Link to='/view/tictactoe'>
                            <button className='py-2 px-4 bg-blue-400 text-white text-xl hover:bg-blue-500 rounded border-b-4 border-blue-600 hover:border-blue-800'>
                                Tic Tac Toe
                            </button>
                        </Link>
                        <Link to='/view/nim'>
                            <button className='py-2 px-4 bg-blue-400 text-white text-xl hover:bg-blue-500 rounded border-b-4 border-blue-600 hover:border-blue-800'>
                                Nim
                            </button>
                        </Link>
                        <Link to='/view/pong'>
                            <button className='py-2 px-4 bg-blue-400 text-white text-xl hover:bg-blue-500 rounded border-b-4 border-blue-600 hover:border-blue-800'>
                                Pong
                            </button>
                        </Link>
                    </div>
                </div>
            </div>
        );
    }
}

export default LeaderboardHub;